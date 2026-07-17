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
# `numpy.ndarray[...]` and `numpy.dtype[...]` only became subscriptable in
# numpy 1.22, when they gained ``__class_getitem__``. We feature-detect on
# that -- rather than compare versions, and rather than test for
# `numpy.typing`, which exists from 1.20 and so would wrongly claim support
# on 1.20 and 1.21.
_SUBSCRIPTABLE = (
    np is not None
    and hasattr(np.ndarray, "__class_getitem__")
    and hasattr(np.dtype, "__class_getitem__")
)


if tx.TYPE_CHECKING or _SUBSCRIPTABLE:
    dtype = np.dtype
    """See [`numpy.dtype`][]."""

    ndarray = np.ndarray
    """See [`numpy.ndarray`][]."""

elif np is not None:  # pragma: no cover
    # numpy < 1.22: the array types are not subscriptable, so we subclass
    # them to add the generic parameters. Note this means `ndarray` is *not*
    # `numpy.ndarray` on these versions, so `isinstance` against it is
    # narrower than you would expect -- check against `numpy.ndarray`.
    #
    # We only ever reach this branch on old numpy, which matters: numpy 2.x
    # forbids subclassing `dtype` ("Preliminary-API: Cannot subclass
    # DType."), so this code must not run there.

    class dtype(np.dtype, tx.Generic[DTYPE]):  # type: ignore[no-redef,misc]
        """See [`numpy.dtype`][]."""

    class ndarray(  # type: ignore[no-redef,misc]
        np.ndarray, tx.Generic[SHAPE, DTYPE]
    ):
        """See [`numpy.ndarray`][]."""

else:  # pragma: no cover

    class dtype(tx.Generic[DTYPE]):  # type: ignore[no-redef]
        """A stub for [`numpy.dtype`][], when numpy is not installed."""

    class ndarray(tx.Generic[SHAPE, DTYPE]):  # type: ignore[no-redef]
        """A stub for [`numpy.ndarray`][], when numpy is not installed."""


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
