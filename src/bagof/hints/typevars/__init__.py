"""Reusable TypeVars.

Modules
-------
co
    Covariant TypeVars.
contra
    Covariant TypeVars.
contra
    Contravariant TypeVars.
inv
    Invariant TypeVars.
infer
    TypeVars with inferred variance.
"""

__all__ = ["co", "contra", "infer", "inv"]

from . import co, contra, infer, inv
