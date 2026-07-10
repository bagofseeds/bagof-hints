__all__ = ["T", "K"]

import typing_extensions as tx

T = tx.TypeVar("T", covariant=True, default=tx.Any)
"""A covariant TypeVar."""

K = tx.TypeVar("K", covariant=True, bound=tx.Hashable)
"""A covariant hashable TypeVar."""
