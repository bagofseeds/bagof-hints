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

import typing_extensions as tx

from ._internal.typevars.inv import DTYPE, SHAPE
from .array import (  # noqa: F401
    ArrayNamespace,
    ArrayProtocol,
    DTypeProtocol,
)
from .numpy import DTypeLike, dtype  # noqa: F401

if tx.TYPE_CHECKING:
    import dask.array as da

else:
    try:
        import dask.array as da
    except ImportError:  # pragma: no cover
        da = None


# Whether dask's array type can be parametrised at runtime (see the note in
# ``bagof.hints.numpy`` on why we detect ``__class_getitem__``).
_SUBSCRIPTABLE = da is not None and hasattr(da.Array, "__class_getitem__")


if tx.TYPE_CHECKING or _SUBSCRIPTABLE:
    Array = da.Array
    """See [`dask.array.Array`][]."""

elif da is not None:

    class Array(  # type: ignore[no-redef,misc]
        da.Array, tx.Generic[SHAPE, DTYPE]
    ):
        """See [`dask.array.Array`][]."""

else:  # pragma: no cover

    class Array(tx.Generic[SHAPE, DTYPE]):  # type: ignore[no-redef]
        """A stub for [`dask.array.Array`][], when dask is not installed."""


NDArray: tx.TypeAlias = Array[tx.Tuple[int, ...], dtype[DTYPE]]
"""A dask array of arbitrary shape, parametrised by its data type."""
