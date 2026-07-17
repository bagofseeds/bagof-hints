"""
Hints for [`numpy`][] arrays and data types.

!!! note
    This module is **not** imported by `bagof.hints`, so that importing the
    package never imports numpy. Import it explicitly:

    ```python
    from bagof.hints import numpy as npt
    ```

    It stays importable when numpy is absent, in which case the array types
    degrade to empty generic stubs, so that annotations still evaluate.
"""
__all__ = [
    "ArrayProtocol",
    "ArrayNamespace",
    "DTypeProtocol",
    "ArrayLike",
    "DTypeLike",
    "dtype",
    "ndarray",
    "NDArray",
    "typevars",
]

import sys

import typing_extensions as tx

from .._internal.typevars.inv import DTYPE, SHAPE
from ..array import ArrayLike as _ArrayLike
from ..array import (  # noqa: F401
    ArrayNamespace,
    ArrayProtocol,
    DTypeProtocol,
)
from ..array import DTypeLike as _DTypeLike
from . import typevars
from ._compat import np, npt

# Whether numpy's array types can be parametrised at runtime.
#
# Two independent gates must both pass:
#   * numpy >= 1.22, which is when ``ndarray`` / ``dtype`` gained
#     ``__class_getitem__`` (``numpy.typing`` alone, present from 1.20,
#     would wrongly claim support on 1.20/1.21); and
#   * Python >= 3.9 -- numpy refuses the subscription on 3.8 with
#     "Type subscription requires python >= 3.9", *even though*
#     ``__class_getitem__`` exists there, so the attribute check alone is a
#     false positive on 3.8.
# When either gate fails we fall back to library-free generic stubs, which
# subscript fine everywhere (subclassing numpy's types is not an option:
# ``dtype`` cannot be subclassed, and a subclassed ``ndarray`` inherits the
# same version gate).
_SUBSCRIPTABLE = (
    np is not None
    and sys.version_info >= (3, 9)
    and hasattr(np.ndarray, "__class_getitem__")
    and hasattr(np.dtype, "__class_getitem__")
)


if tx.TYPE_CHECKING or _SUBSCRIPTABLE:
    dtype = np.dtype
    """See [`numpy.dtype`][]."""

    ndarray = np.ndarray
    """See [`numpy.ndarray`][]."""

else:  # pragma: no cover
    # numpy absent, or its types are not subscriptable (numpy < 1.22, or
    # Python 3.8). ``ndarray`` / ``dtype`` are then generic *stubs* -- not
    # numpy's own types -- so annotations still evaluate, but ``isinstance``
    # against them is meaningless (use ``numpy.ndarray`` or the library-free
    # [`ArrayProtocol`][bagof.hints.array.ArrayProtocol] instead). Not
    # covered on the 3.x coverage run, where the branch above is taken; the
    # 3.8 CI job exercises it instead.

    class dtype(tx.Generic[DTYPE]):  # type: ignore[no-redef]
        """A generic stub for [`numpy.dtype`][]."""

    class ndarray(tx.Generic[SHAPE, DTYPE]):  # type: ignore[no-redef]
        """A generic stub for [`numpy.ndarray`][]."""


NDArray: tx.TypeAlias = ndarray[tx.Tuple[int, ...], dtype[DTYPE]]
"""
An array of arbitrary shape, parametrised by its data type.

!!! note
    Unlike [`numpy.typing.NDArray`][], which is generic over the *scalar*
    type only, this alias keeps both parameters of [`ndarray`][], so that
    `ndarray[Tuple[int, int], dtype[float64]]` and `NDArray[float64]` agree.
"""

if tx.TYPE_CHECKING or npt is not None:
    ArrayLike: tx.TypeAlias = npt.ArrayLike
    """See [`numpy.typing.ArrayLike`][]."""

    DTypeLike: tx.TypeAlias = npt.DTypeLike
    """See [`numpy.typing.DTypeLike`][]."""

else:  # pragma: no cover
    ArrayLike: tx.TypeAlias = _ArrayLike
    """See [`bagof.hints.array.ArrayLike`][]."""

    DTypeLike: tx.TypeAlias = _DTypeLike
    """See [`bagof.hints.array.DTypeLike`][]."""
