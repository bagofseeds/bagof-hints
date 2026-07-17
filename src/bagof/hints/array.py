"""
Protocols for array-like objects, independent of any array library.

The protocols defined here are purely *structural*, so they match numpy,
cupy, dask and any other array library that implements the relevant dunder
-- without importing, or depending on, any of them.

Library-specific hints live in the [`numpy`][bagof.hints.numpy],
[`cupy`][bagof.hints.cupy] and [`dask`][bagof.hints.dask] submodules.
Unlike every other submodule, those are **not** imported by default, so
that `import bagof.hints` never imports an array library.
"""
__all__ = [
    "ArrayProtocol",
    "ArrayNamespace",
    "DTypeProtocol",
    "ArrayLike",
    "DTypeLike",
]
# Import stdlib so that mkdocstring correctly resolves cross-references
import numbers  # noqa: F401

import typing_extensions as tx

from ._internal.typevars.inv import DTYPE


@tx.runtime_checkable
class ArrayProtocol(tx.Protocol):
    """
    An object that can be converted to an array.

    This is the oldest and most widely implemented array hook: numpy, cupy,
    dask, torch and pandas objects all provide it, so a single structural
    check covers them all. See [`numpy.ndarray.__array__`][].
    """

    def __array__(self, *args, **kwargs) -> tx.Any: ...


@tx.runtime_checkable
class ArrayNamespace(tx.Protocol):
    """
    An object that implements the Python array API standard.

    This is the modern, portable alternative to [`ArrayProtocol`][]: rather
    than converting to a numpy array, it exposes the namespace of the
    library that owns the object, so that library-agnostic code can call
    `xp.mean(x)` without knowing which library `x` came from.

    Prefer this over [`ArrayProtocol`][] when the goal is to *stay* in the
    originating library (and off the host, for GPU arrays), since
    `__array__` forces a conversion to numpy.

    See <https://data-apis.org/array-api/latest/>.
    """

    def __array_namespace__(self, *args, **kwargs) -> tx.Any: ...


@tx.runtime_checkable
class DTypeProtocol(tx.Protocol[DTYPE]):
    """
    An object that carries a data type.

    Any array, and any [`numpy.dtype`][]-like object, satisfies this.
    """

    dtype: DTYPE


ArrayLike: tx.TypeAlias = tx.Union[
    numbers.Number, tx.Sequence[tx.Any], ArrayProtocol
]
"""
Anything that can reasonably be turned into an array.

This is the library-agnostic fallback. When numpy is installed,
[`bagof.hints.numpy.ArrayLike`][] is more precise -- it additionally covers
buffers, nested sequences, and the `str`/`bytes` cases.
"""

DTypeLike: tx.TypeAlias = tx.Union[type, str, "DTypeProtocol[tx.Any]"]
"""
Anything that can reasonably be turned into a data type.

This is the library-agnostic fallback. When numpy is installed,
[`bagof.hints.numpy.DTypeLike`][] is more precise -- it additionally covers
structured-dtype specifications such as `[("a", int)]`.
"""
