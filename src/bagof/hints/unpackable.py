import typing_extensions as tx

T = tx.TypeVar("T")


class Unpackable(tx.Protocol[T]):
  """
  A protocol for objects than can be unpacked using the `**` syntax.
  """

  def keys(self) -> tx.Iterable[str]: ...

  def __getitem__(self, key: str) -> VAL: ...
