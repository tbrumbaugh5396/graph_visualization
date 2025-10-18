"""Fallback minimal MVU messaging utilities."""

from enum import Enum
from typing import Any, Callable, Dict, Tuple


class MessageEnum(Enum):
    """Enum base used for app messages; stores tuple(name, *fields)."""
    def __new__(cls, *args):  # type: ignore[no-redef]
        obj = object.__new__(cls)
        obj._value_ = args
        return obj


def make_message(msg: MessageEnum, **kwargs: Any) -> Tuple[MessageEnum, Dict[str, Any]]:
    return (msg, kwargs)


def get_msg_type(message: Tuple[MessageEnum, Dict[str, Any]]) -> MessageEnum:
    return message[0]


def get_msg_data(message: Tuple[MessageEnum, Dict[str, Any]]) -> Dict[str, Any]:
    return message[1]


