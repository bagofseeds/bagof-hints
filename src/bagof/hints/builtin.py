"""
Builtin types (such as builtin subsets of `collections.abc`).
"""

__all__ = [
    "BuiltinSequence",
    "BuiltinIntegral",
    "BuiltinReal",
    "BuiltinNumber",
    "BuiltinScalar",
]

import typing_extensions as tx

from ._internal import FinalAlias
from .typevars import T_co


BuiltinSequence: FinalAlias = tx.Union[tx.Tuple[T_co, ...], tx.List[T_co]]
"""Tuple or List, where all elements have the same type."""

BuiltinIntegral: FinalAlias = int
"""
The builtin integral type: `int`. 
Note that `bool` is a subtype of `int` and is therefore covered here.
"""

BuiltinReal: FinalAlias = tx.Union[BuiltinIntegral, float]
"""Any builtin real number: `int | float`."""

BuiltinNumber: FinalAlias = tx.Union[BuiltinReal, complex]
"""Any builtin number: `int | float | complex`."""

BuiltinScalar: FinalAlias = tx.Union[BuiltinNumber, str]
"""Any builtin "scalar": `int | float | complex | str`."""
