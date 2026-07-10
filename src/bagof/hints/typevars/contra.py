__all__ = ["T", "K"]

import typing_extensions as tx

T = tx.TypeVar("T", contravariant=True, default=tx.Any)
"""A contravariant TypeVar."""

K = tx.TypeVar("K", contravariant=True, bound=tx.Hashable)
"""A contravariant hashable TypeVar."""
