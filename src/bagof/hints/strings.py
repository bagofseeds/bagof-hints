"""String-like objects."""
__all__ = ["BytesLike", "StringLike", "PathLike"]

import os

from typing_extensions import TypeAlias, Union

BytesLike: TypeAlias = Union[bytes, bytearray, memoryview]
"""
Different bytes representations: `#!python (bytes | bytearray | memoryview)`.
"""

StringLike: TypeAlias = Union[str, BytesLike]
"""Strings or bytes: `#!python (str | bytes | bytearray | memoryview)`."""

PathLike: TypeAlias = Union[str, os.PathLike]
"""Strings or paths: `#!python (str | PathLike)`."""
