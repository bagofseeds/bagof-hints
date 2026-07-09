"""String-like objects."""
__all__ = ["BytesLike", "StringLike", "PathLike"]

import os

import typing_extensions as tx

from ._internal import FinalAlias

BytesLike: FinalAlias = tx.Union[bytes, bytearray, memoryview]
"""Different bytes representations: `(bytes | bytearray | memoryview)`."""

StringLike: FinalAlias = tx.Union[str, BytesLike]
"""Strings or bytes: `(str | bytes | bytearray | memoryview)`."""

PathLike: FinalAlias = tx.Union[str, os.PathLike]
"""Strings or paths: `(str | PathLike)`."""
