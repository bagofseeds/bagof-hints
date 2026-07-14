__all__ = ["T", "K"]

import typing_extensions as tx

T = tx.TypeVar("T", default=tx.Any)
"""An invariant TypeVar (with a compact name)."""

K = tx.TypeVar("K", bound=tx.Hashable)
"""An invariant hashable TypeVar (with a compact name)."""
