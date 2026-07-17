"""numpy TypeVars with inferred variance."""

__all__ = []

import typing_extensions as tx

from .._compat import np, npt

if tx.TYPE_CHECKING or np is not None:
    DTYPE = tx.TypeVar("DTYPE", infer_variance=True, bound=np.dtype)
    """An inferred-variance TypeVar for numpy dtypes."""

    __all__.append("DTYPE")

if tx.TYPE_CHECKING or npt is not None:
    DTYPELIKE = tx.TypeVar(
        "DTYPELIKE", infer_variance=True, bound=npt.DTypeLike
    )
    """
    An inferred-variance TypeVar for things convertible to numpy dtypes.
    """

    __all__.append("DTYPELIKE")
