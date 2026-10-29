"""
Hints for [`dask.array`][] arrays.

dask reuses numpy's data types, so this module only defines the array type
itself; `dtype`, `DTypeLike` and the protocols are re-exported from
[`bagof.hints.numpy`][] and [`bagof.hints.array`][].

!!! note
    This module is **not** imported by `bagof.hints`, and importing it does
    not import dask either: each hint is resolved on first access, which is
    when its library is imported (dask for [`Array`][], numpy for
    [`dtype`][], both for [`NDArray`][]). It stays usable when dask is
    absent, in which case [`Array`][] degrades to an empty generic stub.
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

from ._internal.lazy import lazy_attributes
from .array import (  # noqa: F401
    ArrayNamespace,
    ArrayProtocol,
    DTypeProtocol,
)

if tx.TYPE_CHECKING:
    # Import the bare module so mkdocstrings resolves the `dask.array.*`
    # cross-references in the docstrings.
    import dask.array  # noqa: F401, I001

    # Not sorted: the docs list members in import order.
    from ._internal.numpy.arrays import dtype, DTypeLike
    from ._internal.dask import Array, NDArray

else:
    __getattr__, __dir__ = lazy_attributes(
        __name__,
        {
            "DTypeLike": "bagof.hints._internal.numpy.arrays",
            "dtype": "bagof.hints._internal.numpy.arrays",
            "Array": "bagof.hints._internal.dask",
            "NDArray": "bagof.hints._internal.dask",
        },
    )
