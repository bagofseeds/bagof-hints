"""Types related to JSON (de)serialization."""
__all__ = [
    "JSONNumber",
    "JSONScalar",
    "JSON",
    "JSONDict",
    "MutableJSON",
    "MutableJSONDict",
]
# Import stdlib so that mkdocstring correctly resolves cross-references
import json  # noqa: F401

from typing_extensions import Dict, List, Mapping, TypeAlias, Union

from .builtin import BuiltinSequence

JSONNumber: TypeAlias = Union[int, float]
"""
A number that is properly handled by [`json.dump`][]:
`#!python (int | float)`.
"""

JSONScalar: TypeAlias = Union[int, float, bool, str, None]
"""
A scalar that is properly handled by [`json.dump`][]:
`#!python (int | float | str | None)`.
"""

JSON: TypeAlias = Union[
    # Not a TypeAlias because of recursion
    JSONScalar,
    Mapping[str, "JSON"],
    BuiltinSequence["JSON"],
]
"""
A value that is properly handled by [`json.dump`][]:
`#!python JSON = JSONScalar | Dict[str, JSON] | List[JSON] | Tuple[JSON, ...]`.
Note that this is a recursive type.
"""

JSONDict: TypeAlias = Mapping[str, JSON]
"""A JSON dictionary."""

MutableJSON: TypeAlias = Union[
    # Not a TypeAlias because of recursion
    JSONScalar,
    Dict[str, "MutableJSON"],
    List["MutableJSON"],
]
"""A JSON value, where all structures (arrays and objects) are mutable."""

MutableJSONDict: TypeAlias = Dict[str, MutableJSON]
"""A mutable JSON dictionary."""
