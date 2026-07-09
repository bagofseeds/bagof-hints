import typing_extensions as tx

FinalAlias: tx.Final[tx.TypeAlias] = tx.Final[tx.TypeAlias]
FinalTypeVar: FinalAlias = tx.Final[tx.TypeVar]