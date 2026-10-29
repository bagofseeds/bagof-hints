"""
Lazily resolved module attributes (PEP 562).

The array hints (``bagof.hints.numpy`` / ``cupy`` / ``dask``) are defined in
private ``_internal`` modules, which import their array library as soon as
they are loaded. The public modules only *name* those hints, and resolve
each of them on first access through a module-level ``__getattr__``, so that
importing a public module never imports numpy, cupy or dask: only accessing
one of their hints does.
"""
import importlib
import sys

import typing_extensions as tx

__all__ = ["lazy_attributes"]


def lazy_attributes(
    module: str, sources: tx.Mapping[str, str]
) -> tx.Tuple[tx.Callable[[str], tx.Any], tx.Callable[[], tx.List[str]]]:
    """
    Build the module-level ``__getattr__`` and ``__dir__`` of a lazy module.

    Parameters
    ----------
    module
        Name of the public module, i.e. its ``__name__``.
    sources
        Maps each lazy attribute to the module that defines it (under the
        same name). That module is only imported when one of its attributes
        is first accessed. They are then all cached in the public module's
        namespace, so that later accesses bypass ``__getattr__``.

    Returns
    -------
    __getattr__
        Resolves the lazy attributes.
    __dir__
        Lists the public API (``__all__``, or the lazy attributes if
        ``__all__`` is itself lazy) without resolving anything.
    """
    namespace = vars(sys.modules[module])

    def __getattr__(name: str) -> tx.Any:
        if name in sources:
            importlib.import_module(sources[name])
            # Bind every lazy attribute whose source is now loaded, not just
            # this one, so that the namespace reflects what has already been
            # imported. Tools that read the module dict to avoid triggering
            # imports (e.g., forward-reference registries) then see them all.
            for attr, source in sources.items():
                loaded = sys.modules.get(source)
                if attr not in namespace and hasattr(loaded, attr):
                    namespace[attr] = getattr(loaded, attr)
        # Missing if unknown, or if its source only defines it when the
        # array library is installed (e.g., the numpy-bound TypeVars).
        if name not in namespace:
            raise AttributeError(
                f"module {module!r} has no attribute {name!r}"
            )
        return namespace[name]

    def __dir__() -> tx.List[str]:
        if "__all__" in namespace:
            return sorted(namespace["__all__"])
        return sorted(name for name in sources if not name.startswith("__"))

    return __getattr__, __dir__
