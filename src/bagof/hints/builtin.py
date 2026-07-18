"""
Builtin types (such as builtin subsets of [`collections.abc`][]).
"""

__all__ = [
    "BuiltinSequence",
    "BuiltinIntegral",
    "BuiltinReal",
    "BuiltinNumber",
    "BuiltinScalar",
]
# Import stdlib so that mkdocstring correctly resolves cross-references
import collections.abc  # noqa: F401

from typing_extensions import List, Tuple, TypeAlias, Union

from ._internal.typevars.co import T as T_co

BuiltinSequence: TypeAlias = Union[Tuple[T_co, ...], List[T_co]]
"""Tuple or List, where all elements have the same type."""

BuiltinIntegral: TypeAlias = int
"""
The builtin integral type: `#!python int`.

!!! note
    `#!python bool` is a subtype of `#!python int` and is therefore
    covered here.
"""

BuiltinReal: TypeAlias = Union[BuiltinIntegral, float]
"""Any builtin real number: `#!python (int | float)`."""

BuiltinNumber: TypeAlias = Union[BuiltinReal, complex]
"""Any builtin number: `#!python (int | float | complex)`."""

BuiltinScalar: TypeAlias = Union[BuiltinNumber, str]
"""
Any builtin "scalar": `#!python (int | float | complex | str)`.

!!! example
    The alias flattens to its member types:

    ```python
    >>> from typing import get_args
    >>> from bagof.hints.builtin import BuiltinScalar
    >>> get_args(BuiltinScalar)
    (<class 'int'>, <class 'float'>, <class 'complex'>, <class 'str'>)
    ```
"""
