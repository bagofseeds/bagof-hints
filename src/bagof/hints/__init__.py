"""Reusable typing hints for Python projects."""

import os

import typing_extensions as tx

try:
    from ._version import __version__
except ImportError:  # pragma: no cover
    __version__ = "0+unknown"

__all__ = [
    "__version__",
    "T",
    "OneOrIter",
    "OneOrSeq",
    "BuiltinSequence",
    "BuiltinIntegral",
    "BuiltinReal",
    "BuiltinNumber",
    "BuiltinScalar",
    "BytesLike",
    "StringLike",
    "PathLike",
    "JSONNumber",
    "JSONNumberLike",
    "JSONScalar",
    "JSON",
    "JSONDict",
    "FrozenJSON",
    "FrozenJSONDict",
    "MutableJSON",
    "MutableJSONDict",
]

T = tx.TypeVar("T")

OneOrIter = tx.Union[T, tx.Iterable[T]]
OneOrSeq = tx.Union[T, tx.Sequence[T]]
BuiltinSequence = tx.Union[tx.Tuple[T, ...], tx.List[T]]

BuiltinIntegral: tx.TypeAlias = int
BuiltinReal: tx.TypeAlias = tx.Union[int, float]
BuiltinNumber: tx.TypeAlias = tx.Union[BuiltinReal, complex]
BuiltinScalar: tx.TypeAlias = tx.Union[BuiltinNumber, str]

BytesLike: tx.TypeAlias = tx.Union[bytes, bytearray, memoryview]
StringLike: tx.TypeAlias = tx.Union[str, BytesLike]
PathLike: tx.TypeAlias = tx.Union[str, os.PathLike]

JSONNumber: tx.TypeAlias = tx.Union[int, float]
JSONNumberLike: tx.TypeAlias = tx.Union[int, float, bool]
JSONScalar: tx.TypeAlias = tx.Union[int, float, bool, str, None]
JSON: tx.TypeAlias = tx.Union[
    JSONScalar,
    tx.Mapping[str, "JSON"],
    BuiltinSequence["JSON"],
]
JSONDict: tx.TypeAlias = tx.Mapping[str, JSON]

FrozenJSON: tx.TypeAlias = tx.Union[
    JSONScalar,
    tx.Mapping[str, "FrozenJSON"],
    tx.Tuple["FrozenJSON", ...],
]
FrozenJSONDict: tx.TypeAlias = tx.Mapping[str, FrozenJSON]

MutableJSON: tx.TypeAlias = tx.Union[
    JSONScalar,
    tx.MutableMapping[str, "MutableJSON"],
    tx.List["MutableJSON"],
]
MutableJSONDict: tx.TypeAlias = tx.MutableMapping[str, MutableJSON]
