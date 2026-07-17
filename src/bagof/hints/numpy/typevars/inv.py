"""Invariant numpy TypeVars."""

__all__ = []

import typing_extensions as tx

from .._compat import np, npt

if tx.TYPE_CHECKING or np is not None:
    DTYPE = tx.TypeVar("DTYPE", bound=np.dtype)
    """An invariant TypeVar for numpy dtypes."""

    __all__.append("DTYPE")

if tx.TYPE_CHECKING or npt is not None:
    DTYPELIKE = tx.TypeVar("DTYPELIKE", bound=npt.DTypeLike)
    """
    An invariant TypeVar for things that can be converted to numpy dtypes.
    """

    __all__.append("DTYPELIKE")
