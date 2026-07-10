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

from .typevars.co import T as T_co

BuiltinSequence: tx.TypeAlias = tx.Union[tx.Tuple[T_co, ...], tx.List[T_co]]
"""Tuple or List, where all elements have the same type."""

BuiltinIntegral: tx.TypeAlias = int
"""
The builtin integral type: `int`.
Note that `bool` is a subtype of `int` and is therefore covered here.
"""

BuiltinReal: tx.TypeAlias = tx.Union[BuiltinIntegral, float]
"""Any builtin real number: `int | float`."""

BuiltinNumber: tx.TypeAlias = tx.Union[BuiltinReal, complex]
"""Any builtin number: `int | float | complex`."""

BuiltinScalar: tx.TypeAlias = tx.Union[BuiltinNumber, str]
"""Any builtin "scalar": `int | float | complex | str`."""
