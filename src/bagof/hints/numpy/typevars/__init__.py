"""
numpy-specific TypeVars, in the four variance flavours.

These carry numpy-derived bounds (``np.dtype`` / ``numpy.typing.DTypeLike``)
and so live under [`bagof.hints.numpy`][] rather than the top-level
[`bagof.hints.typevars`][], keeping the latter importable without numpy.

Modules
-------
co
    Covariant TypeVars.
contra
    Contravariant TypeVars.
infer
    TypeVars with inferred variance.
inv
    Invariant TypeVars.
"""

__all__ = ["co", "contra", "infer", "inv"]

from . import co, contra, infer, inv
