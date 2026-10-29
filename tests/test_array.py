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


def _run_fresh(code: str) -> None:
    # Checked in a fresh interpreter: importing this test module already
    # imported numpy (via ``importorskip``), so an in-process ``sys.modules``
    # check would be meaningless.
    code = (
        "import sys\n"
        "def loaded():\n"
        "    return {'numpy', 'cupy', 'dask'} & set(sys.modules)\n"
    ) + code
    result = subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_import_hints_does_not_import_array_libraries() -> None:
    _run_fresh("import bagof.hints\nassert not loaded(), loaded()\n")


def test_import_array_submodules_does_not_import_array_libraries() -> None:
    # Importing the submodules, listing them, and using their library-free
    # protocols must not import anything: only accessing a hint does.
    _run_fresh(
        "import bagof.hints as hints\n"
        "from bagof.hints.numpy.typevars import co, contra, infer, inv\n"
        "for name in ('numpy', 'cupy', 'dask'):\n"
        "    mod = getattr(hints, name)\n"
        "    assert 'NDArray' in dir(mod), dir(mod)\n"
        "    assert mod.ArrayProtocol is hints.ArrayProtocol\n"
        "assert 'DTYPE' in dir(co), dir(co)\n"
        "hints.numpy.typevars.inv\n"
        "assert not loaded(), loaded()\n"
    )


@pytest.mark.parametrize(
    "module,name,expected",
    [
        ("numpy", "ndarray", "{'numpy'}"),
        ("numpy", "ArrayLike", "{'numpy'}"),
        ("numpy.typevars.co", "DTYPE", "{'numpy'}"),
        ("numpy.typevars.inv", "__all__", "{'numpy'}"),
        # dask reuses numpy's dtypes, so its ``dtype`` only needs numpy...
        ("dask", "dtype", "{'numpy'}"),
        # ... while its array type needs dask (and numpy, for ``NDArray``).
        ("dask", "NDArray", "{'numpy', 'dask'}"),
    ],
)
def test_accessing_a_hint_imports_its_library(
    module: str, name: str, expected: str
) -> None:
    if "dask" in expected:
        pytest.importorskip("dask.array")
    _run_fresh(
        f"from bagof.hints import {module.split('.')[0]}\n"
        f"import bagof.hints.{module} as mod\n"
        "assert not loaded(), loaded()\n"
        f"getattr(mod, {name!r})\n"
        f"assert loaded() == {expected}, loaded()\n"
    )


def test_accessing_a_hint_binds_its_loaded_siblings() -> None:
    # Once a source module is loaded, all of its hints are bound in the
    # public namespace, so that tools reading ``vars(module)`` (to avoid
    # triggering ``__getattr__``) see e.g. ``Array`` after ``NDArray``.
    pytest.importorskip("dask.array")
    _run_fresh(
        "from bagof.hints import dask, numpy\n"
        "dask.NDArray\n"
        "bound = set(vars(dask))\n"
        "assert {'Array', 'NDArray', 'dtype', 'DTypeLike'} <= bound, bound\n"
        "assert 'ndarray' not in vars(numpy)\n"
        "numpy.ArrayLike\n"
        "assert 'ndarray' in vars(numpy)\n"
    )


def test_numpy_typevars_export_nothing_without_numpy() -> None:
    # Blocking the import simulates an environment without numpy.
    _run_fresh(
        "sys.modules['numpy'] = None\n"
        "from bagof.hints.numpy.typevars import co\n"
        "assert co.__all__ == [], co.__all__\n"
        "assert not hasattr(co, 'DTYPE')\n"
        "namespace = {}\n"
        "exec('from bagof.hints.numpy.typevars.co import *', namespace)\n"
        "assert 'DTYPE' not in namespace\n"
    )


@pytest.mark.parametrize("name", ["numpy", "cupy", "dask"])
def test_lazy_hints_are_cached_and_unknown_names_raise(name: str) -> None:
    mod = importlib.import_module(f"bagof.hints.{name}")
    # Resolved once, then stored in the module namespace, so that later
    # accesses bypass ``__getattr__``.
    assert mod.__getattr__("NDArray") is vars(mod)["NDArray"]
    with pytest.raises(AttributeError):
        _ = mod.does_not_exist


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


def test_numpy_array_types_match_subscriptability() -> None:
    from bagof.hints import numpy as npt
    from bagof.hints._internal.numpy.arrays import _SUBSCRIPTABLE

    if _SUBSCRIPTABLE:
        # numpy >= 1.22 on Python >= 3.9: the hints ARE numpy's own types,
        # so ``isinstance`` and registry-key identity work naturally.
        assert npt.ndarray is numpy.ndarray
        assert npt.dtype is numpy.dtype
        assert isinstance(numpy.zeros(3), npt.ndarray)
    else:  # pragma: no cover
        # Python 3.8 / old numpy: subscriptable generic stubs instead. Not
        # reached on the 3.x coverage run; exercised by the 3.8 CI job.
        assert npt.ndarray is not numpy.ndarray
        assert issubclass(npt.ndarray, tx.Generic)


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
# uses the generic stub)
# ----------------------------------------------------------------------


def test_dask_array_is_a_subscriptable_stub() -> None:
    pytest.importorskip("dask.array")
    from bagof.hints import dask as dkt

    # dask.Array carries no ``__class_getitem__``, so ``dkt.Array`` is a
    # library-free generic stub -- which IS subscriptable.
    assert issubclass(dkt.Array, tx.Generic)
    assert dkt.NDArray[numpy.float64]
    # dtype is shared with the numpy submodule (whichever form it takes).
    from bagof.hints import numpy as npt

    assert dkt.dtype is npt.dtype


def test_dask_array_matches_array_protocol() -> None:
    dask_array = pytest.importorskip("dask.array")
    from bagof.hints import ArrayProtocol

    x = dask_array.from_array(numpy.zeros(3))
    # The library-agnostic protocol is the right isinstance target: it
    # matches the real dask array, whereas the ``dkt.Array`` stub does not.
    assert isinstance(x, ArrayProtocol)
