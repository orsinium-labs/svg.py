from enum import Enum
from typing import Any


def as_str(val: Any) -> str:
    if val is None:
        return ''
    if isinstance(val, Enum):
        return val.value
    if isinstance(val, (list, tuple)):
        return ','.join(as_str(v) for v in val)
    return str(val)
