import importlib.util

__all__ = ["path"]

_spec = importlib.util.find_spec("sqlite_veccie.veccie")
assert _spec is not None
assert _spec.origin is not None

path: str = _spec.origin
"""
The Path of a shared library/DLL containing the veccie sqlite extension.
"""
