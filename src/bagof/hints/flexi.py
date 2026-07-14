"""Flexible "type-like" for use in converters."""
__all__ = ["OneOrIter", "OneOrSeq"]

from typing_extensions import Iterable, Sequence, TypeAlias, Union

from .typevars.co import T as T_co

OneOrIter: TypeAlias = Union[T_co, Iterable[T_co]]
"""A value of a given type, or an iterable of this type."""

OneOrSeq: TypeAlias = Union[T_co, Sequence[T_co]]
"""A value of a given type, or a sequence of this type."""
