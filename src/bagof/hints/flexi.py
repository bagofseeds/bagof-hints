"""Flexible "type-like" for use in converters."""
__all__ = ["OneOrIter", "OneOrSeq"]

import typing_extensions as tx

from .typevars import T_co

OneOrIter: tx.TypeAlias = tx.Union[T_co, tx.Iterable[T_co]]
"""A value of a given type, or an iterable of this type."""

OneOrSeq: tx.TypeAlias = tx.Union[T_co, tx.Sequence[T_co]]
"""A value of a given type, or a sequence of this type."""
