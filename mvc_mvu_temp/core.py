"""Fallback minimal MVU core interfaces.

This is a lightweight stand-in to allow running the app without the external
MVC_MVU framework. It provides basic types used by the app's MVU modules.
"""

from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar


M = TypeVar("M")


class Model:
    """Marker base class for MVU models."""
    pass


@dataclass
class UpdateResult(Generic[M]):
    model: M
    commands: Optional[List[object]] = None


