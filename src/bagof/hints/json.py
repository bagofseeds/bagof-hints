"""Types related to JSON (de)serialization."""
__all__ = [
    "JSONNumber",
    "JSONScalar",
    "JSON",
    "JSONDict",
    "MutableJSON",
    "MutableJSONDict",
    # "ImmutableJSON",
    # "ImmutableJSONDict",
]

import typing_extensions as tx

from .builtin import BuiltinSequence

JSONNumber: tx.TypeAlias = tx.Union[int, float]
"""
A number that is properly handled by [`json.dump`][json.dump]:
`(int | float)`.
"""

JSONScalar: tx.TypeAlias = tx.Union[int, float, bool, str, None]
"""
A scalar that is properly handled by [`json.dump`][json.dump]:
`(int | float | str | None)`.
"""

JSON: tx.TypeAlias = tx.Union[
    # Not a tx.TypeAlias because of recursion
    JSONScalar,
    tx.Mapping[str, "JSON"],
    BuiltinSequence["JSON"],
]
"""
A value that is properly handled by [`json.dump`][json.dump]:
`JSON = JSONScalar | Dict[str, JSON] | List[JSON] | Tuple[JSON, ...]`.
Note that this is a recursive type.
"""

JSONDict: tx.TypeAlias = tx.Mapping[str, JSON]
"""A JSON dictionary."""

MutableJSON: tx.TypeAlias = tx.Union[
    # Not a tx.TypeAlias because of recursion
    JSONScalar,
    tx.Dict[str, "MutableJSON"],
    tx.List["MutableJSON"],
]
"""A JSON value, where all structures (arrays and objects) are mutable."""

MutableJSONDict: tx.TypeAlias = tx.Dict[str, MutableJSON]
"""A mutable JSON dictionary."""


# ImmutableJSON: tx.TypeAlias = tx.Union[
#     # Not a tx.TypeAlias because of recursion
#     JSONScalar,
#     ImmutableMapping[str, "ImmutableJSON"],
#     tx.Tuple["ImmutableJSON", ...],
# ]
# """A JSON value, where all structures (arrays and objects) are immutable."""
#
# ImmutableJSONDict: tx.TypeAlias = ImmutableMapping[str, ImmutableJSON]
# """An immutable JSON dictionary."""
