"""
Hints for [`dask.array`][] arrays.

dask reuses numpy's data types, so this module only defines the array type
itself; `dtype`, `DTypeLike` and the protocols are re-exported from
[`bagof.hints.numpy`][] and [`bagof.hints.array`][].

!!! note
    This module is **not** imported by `bagof.hints`, so that importing the
    package never imports dask. It stays importable when dask is absent, in
    which case [`Array`][] degrades to an empty generic stub.
"""
__all__ = [
    "ArrayProtocol",
    "ArrayNamespace",
    "DTypeProtocol",
    "DTypeLike",
    "dtype",
    "Array",
    "NDArray",
]

import sys

import typing_extensions as tx

from ._internal.typevars.inv import DTYPE, SHAPE
from .array import (  # noqa: F401
    ArrayNamespace,
    ArrayProtocol,
    DTypeProtocol,
)
from .numpy import DTypeLike, dtype  # noqa: F401

if tx.TYPE_CHECKING:
    # Import the bare module so mkdocstrings resolves the `dask.array.*`
    # cross-references in the docstrings below.
    import dask.array  # noqa: F401
    import dask.array as da

else:
    try:
        import dask.array as da
    except ImportError:  # pragma: no cover
        da = None


# Whether dask's array type can be parametrised at runtime (see the note in
# ``bagof.hints.numpy`` on the two gates). dask's ``Array`` has no
# ``__class_getitem__`` at all today, so this is currently always False and
# the generic stub is used -- for `isinstance`, use the real
# ``dask.array.Array`` or the library-free
# [`ArrayProtocol`][bagof.hints.array.ArrayProtocol].
_SUBSCRIPTABLE = (
    da is not None
    and sys.version_info >= (3, 9)
    and hasattr(da.Array, "__class_getitem__")
)


if tx.TYPE_CHECKING or _SUBSCRIPTABLE:  # pragma: no cover
    Array = da.Array
    """See [`dask.array.Array`][]."""

else:

    class Array(tx.Generic[SHAPE, DTYPE]):  # type: ignore[no-redef]
        """A generic stub for [`dask.array.Array`][]."""


NDArray: tx.TypeAlias = Array[tx.Tuple[int, ...], dtype[DTYPE]]
"""A dask array of arbitrary shape, parametrised by its data type."""
