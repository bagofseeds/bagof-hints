"""Reusable TypeVars.

Modules
-------
inv
    Invariant TypeVars.
co
    Covariant TypeVars.
contra
    Contravariant TypeVars.
infer
    TypeVars with inferred variance.
"""

__all__ = ["co", "contra", "infer", "inv"]

from . import co, contra, infer, inv
