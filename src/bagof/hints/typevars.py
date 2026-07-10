"""Reusable TypeVars."""
__all__ = ["T_co", "T_contra"]

import typing_extensions as tx

T_co = tx.TypeVar("T", covariant=True, default=tx.Any)
"""A covariant TypeVar."""

T_contra = tx.TypeVar("T", contravariant=True, default=tx.Any)
"""A contravariant TypeVar."""

K_co = tx.TypeVar("K", covariant=True, bound=tx.Hashable)
"""A covariant hashable TypeVar."""

K_contra = tx.TypeVar("K", contravariant=True, bound=tx.Hashable)
"""A contravariant hashable TypeVar."""
