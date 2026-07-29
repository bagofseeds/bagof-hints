"""
numpy-specific TypeVars.

They come in the same four flavours as [`bagof.hints.typevars`][] --
covariant, contravariant, invariant and inferred-variance -- and carry
numpy-derived bounds ([`numpy.dtype`][] / [`numpy.typing.DTypeLike`][]).
They therefore live under [`bagof.hints.numpy`][] rather than the
top-level [`bagof.hints.typevars`][], keeping the latter importable
without numpy.

!!! note
    Each module only defines the TypeVars whose bound is available:
    `DTYPE` needs numpy, and `DTYPELIKE` needs `numpy.typing` as well.
    When numpy is absent, the modules still import, but export nothing.

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
