"""
Hints for [`cupy`][] arrays.

cupy reuses numpy's data types, so this module only defines the array type
itself; `dtype`, `DTypeLike` and the protocols are re-exported from
[`bagof.hints.numpy`][] and [`bagof.hints.array`][].

!!! note
    This module is **not** imported by `bagof.hints`, so that importing the
    package never imports cupy. It stays importable when cupy is absent, in
    which case [`ndarray`][] degrades to an empty generic stub.
"""
__all__ = [
    "ArrayProtocol",
    "ArrayNamespace",
    "DTypeProtocol",
    "DTypeLike",
    "dtype",
    "ndarray",
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
    import cupy as cp

else:
    try:
        import cupy as cp
    except ImportError:  # pragma: no cover
        cp = None


# Whether cupy's array type can be parametrised at runtime (see the note in
# ``bagof.hints.numpy`` on the two gates; cupy mirrors numpy's behaviour).
_SUBSCRIPTABLE = (
    cp is not None
    and sys.version_info >= (3, 9)
    and hasattr(cp.ndarray, "__class_getitem__")
)


if tx.TYPE_CHECKING or _SUBSCRIPTABLE:  # pragma: no cover
    # cupy is not installable in CI (it needs a CUDA toolchain), so the
    # library-present branch is only ever type-checked, never run.
    ndarray = cp.ndarray
    """See [`cupy.ndarray`][]."""

else:

    class ndarray(tx.Generic[SHAPE, DTYPE]):  # type: ignore[no-redef]
        """A generic stub for [`cupy.ndarray`][]."""


NDArray: tx.TypeAlias = ndarray[tx.Tuple[int, ...], dtype[DTYPE]]
"""A cupy array of arbitrary shape, parametrised by its data type."""
