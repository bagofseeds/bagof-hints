"""Objects unpackable into keyword arguments."""
__all__ = ["Unpackable"]

import typing_extensions as tx

from .typevars import T_co


class Unpackable(tx.Protocol[T_co]):
  """
  A protocol for objects than can be unpacked using the `**` syntax.
  """

  def keys(self) -> tx.Iterable[str]: ...

  def __getitem__(self, key: str) -> T_co: ...
