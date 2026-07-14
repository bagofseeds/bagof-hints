"""Reusable TypeVars.

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
