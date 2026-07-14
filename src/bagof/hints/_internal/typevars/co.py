__all__ = ["T", "K"]

import typing_extensions as tx

T = tx.TypeVar("T", covariant=True, default=tx.Any)
"""A covariant TypeVar (with a compact name)."""

K = tx.TypeVar("K", covariant=True, bound=tx.Hashable)
"""A covariant hashable TypeVar (with a compact name)."""
