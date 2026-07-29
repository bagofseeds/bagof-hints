"""Flexible "type-like" aliases for use in converters."""
__all__ = ["OneOrIter", "OneOrSeq"]

from typing_extensions import Iterable, Sequence, TypeAlias, Union

from ._internal.typevars.co import T as T_co

OneOrIter: TypeAlias = Union[T_co, Iterable[T_co]]
"""A value of a given type, or an iterable of values of that type."""

OneOrSeq: TypeAlias = Union[T_co, Sequence[T_co]]
"""A value of a given type, or a sequence of values of that type."""
