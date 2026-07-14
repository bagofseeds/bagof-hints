__all__ = ["T", "K"]

import typing_extensions as tx

T = tx.TypeVar("T", default=tx.Any, infer_variance=True)
"""A TypeVar whose variance is inferred (with a compact name)."""

K = tx.TypeVar("K", bound=tx.Hashable, infer_variance=True)
"""An hashable TypeVar whose variance is inferred (with a compact name)."""
