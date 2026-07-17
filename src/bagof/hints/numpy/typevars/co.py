"""Covariant numpy TypeVars."""

__all__ = []

import typing_extensions as tx

from .._compat import np, npt

if tx.TYPE_CHECKING or np is not None:
    DTYPE = tx.TypeVar("DTYPE", covariant=True, bound=np.dtype)
    """A covariant TypeVar for numpy dtypes."""

    __all__.append("DTYPE")

if tx.TYPE_CHECKING or npt is not None:
    DTYPELIKE = tx.TypeVar("DTYPELIKE", covariant=True, bound=npt.DTypeLike)
    """A covariant TypeVar for things that can be converted to numpy dtypes."""

    __all__.append("DTYPELIKE")
