"""
Tests for the array hints and their lazy, optional-dependency behaviour.

The central contract: importing ``bagof.hints`` must not import any array
library, yet the ``numpy`` / ``cupy`` / ``dask`` submodules stay importable
(degrading to stubs) whether or not their library is installed.
"""

from __future__ import annotations

import importlib
import subprocess
import sys

import pytest
import typing_extensions as tx

import bagof.hints as hints

numpy = pytest.importorskip("numpy")


# ----------------------------------------------------------------------
# Lazy-import contract
# ----------------------------------------------------------------------


def test_import_hints_does_not_import_array_libraries() -> None:
    # Checked in a fresh interpreter: importing this test module already
    # imported numpy (via ``importorskip``), so an in-process ``sys.modules``
    # check would be meaningless.
    code = (
        "import sys, bagof.hints\n"
        "leaked = {'numpy', 'cupy', 'dask'} & set(sys.modules)\n"
        "assert not leaked, leaked\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True
    )
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize("name", ["numpy", "cupy", "dask"])
def test_lazy_submodules_are_declared_but_not_eager(name: str) -> None:
    # Declared in ``__all__`` so they are discoverable...
    assert name in hints.__all__
    # ... and resolvable as attributes (PEP 562 ``__getattr__``)...
    assert importlib.import_module(f"bagof.hints.{name}") is getattr(
        hints, name
    )
    # ... and marked lazy, so they are excluded from the eager import block.
    assert name in hints._LAZY_MODULES


def test_unknown_attribute_still_raises() -> None:
    with pytest.raises(AttributeError):
        _ = hints.does_not_exist


def test_getattr_resolves_lazy_submodule_in_process() -> None:
    # Call ``__getattr__`` directly: once any test has imported the
    # submodule, Python caches it as an attribute and never re-enters
    # ``__getattr__``, so plain ``hints.numpy`` would not exercise it.
    assert hints.__getattr__("numpy") is importlib.import_module(
        "bagof.hints.numpy"
    )
    with pytest.raises(AttributeError):
        hints.__getattr__("nope")


def test_dir_lists_public_api() -> None:
    listing = dir(hints)
    assert "numpy" in listing
    assert "ArrayProtocol" in listing
    assert listing == sorted(listing)


# ----------------------------------------------------------------------
# Library-agnostic protocols (always importable, no array library needed)
# ----------------------------------------------------------------------


@pytest.mark.parametrize(
    "protocol_name", ["ArrayProtocol", "ArrayNamespace", "DTypeProtocol"]
)
def test_protocols_are_exported_eagerly(protocol_name: str) -> None:
    # These live in ``hints.array`` and are numpy-free, so they are part of
    # the eager top-level API.
    assert hasattr(hints, protocol_name)


def test_array_protocol_matches_numpy_array() -> None:
    from bagof.hints import ArrayProtocol

    assert isinstance(numpy.zeros(3), ArrayProtocol)
    assert not isinstance([1, 2, 3], ArrayProtocol)


def test_array_namespace_matches_numpy_array() -> None:
    from bagof.hints import ArrayNamespace

    # numpy implements the array API standard from 2.0 onwards.
    if hasattr(numpy.zeros(3), "__array_namespace__"):
        assert isinstance(numpy.zeros(3), ArrayNamespace)
    assert not isinstance(object(), ArrayNamespace)


def test_dtype_protocol_matches_anything_with_a_dtype() -> None:
    from bagof.hints import DTypeProtocol

    assert isinstance(numpy.zeros(3), DTypeProtocol)
    assert not isinstance(object(), DTypeProtocol)


# ----------------------------------------------------------------------
# numpy submodule
# ----------------------------------------------------------------------


def test_numpy_array_types_are_the_real_thing() -> None:
    from bagof.hints import numpy as npt

    # On a subscriptable numpy (>=1.22), the hints ARE numpy's own types, so
    # ``isinstance`` and registry-key identity work naturally.
    assert npt.ndarray is numpy.ndarray
    assert npt.dtype is numpy.dtype
    assert isinstance(numpy.zeros(3), npt.ndarray)


def test_numpy_ndarray_is_subscriptable() -> None:
    from bagof.hints import numpy as npt

    # The alias keeps BOTH parameters (shape, dtype), unlike
    # ``numpy.typing.NDArray`` which is generic over the scalar only.
    assert npt.NDArray[numpy.float64] is not None
    assert npt.ndarray[tx.Tuple[int, int], npt.dtype[numpy.float64]]


def test_numpy_dtype_like_prefers_numpy_typing() -> None:
    from bagof.hints import numpy as npt

    # When numpy.typing is available, DTypeLike/ArrayLike defer to it.
    assert npt.DTypeLike is numpy.typing.DTypeLike
    assert npt.ArrayLike is numpy.typing.ArrayLike


# ----------------------------------------------------------------------
# numpy TypeVars (moved out of the eager typevars, into hints.numpy)
# ----------------------------------------------------------------------


@pytest.mark.parametrize("variance", ["co", "contra", "inv", "infer"])
def test_numpy_typevars_carry_dtype_bound(variance: str) -> None:
    mod = importlib.import_module(f"bagof.hints.numpy.typevars.{variance}")
    assert "DTYPE" in mod.__all__
    assert "DTYPELIKE" in mod.__all__
    assert isinstance(mod.DTYPE, tx.TypeVar)
    assert mod.DTYPE.__bound__ is numpy.dtype


@pytest.mark.parametrize(
    "variance,flag",
    [
        ("co", "__covariant__"),
        ("contra", "__contravariant__"),
    ],
)
def test_numpy_typevars_variance(variance: str, flag: str) -> None:
    mod = importlib.import_module(f"bagof.hints.numpy.typevars.{variance}")
    assert getattr(mod.DTYPE, flag) is True


# ----------------------------------------------------------------------
# dask submodule (installed, but its Array is not subscriptable, so it
# exercises the generic-subclass fallback that numpy never reaches)
# ----------------------------------------------------------------------


def test_dask_array_is_subscriptable_via_fallback() -> None:
    dask_array = pytest.importorskip("dask.array")
    from bagof.hints import dask as dkt

    # dask.Array is not subscriptable at runtime, so ``dkt.Array`` is a
    # generic subclass of it -- which IS subscriptable.
    assert issubclass(dkt.Array, dask_array.Array)
    assert dkt.NDArray[numpy.float64]
    # dtype and the protocols are shared with numpy.
    assert dkt.dtype is numpy.dtype


def test_dask_array_matches_array_protocol() -> None:
    dask_array = pytest.importorskip("dask.array")
    from bagof.hints import ArrayProtocol

    x = dask_array.from_array(numpy.zeros(3))
    # The library-agnostic protocol is the right isinstance target -- it
    # matches the real dask array, whereas ``dkt.Array`` (a subclass) does
    # not.
    assert isinstance(x, ArrayProtocol)
