"""String-like objects."""
__all__ = ["BytesLike", "StringLike", "PathLike"]

import os

import typing_extensions as tx

BytesLike: tx.TypeAlias = tx.Union[bytes, bytearray, memoryview]
"""Different bytes representations: `(bytes | bytearray | memoryview)`."""

StringLike: tx.TypeAlias = tx.Union[str, BytesLike]
"""Strings or bytes: `(str | bytes | bytearray | memoryview)`."""

PathLike: tx.TypeAlias = tx.Union[str, os.PathLike]
"""Strings or paths: `(str | PathLike)`."""
