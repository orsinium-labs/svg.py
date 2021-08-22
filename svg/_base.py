from dataclasses import dataclass
from enum import Enum
from typing import Any


@dataclass
class Base:
    """"

    Schema:
    https://github.com/dumistoklus/svg-xsd-schema/blob/master/svg.xsd
    """
    ...

    @classmethod
    def _as_str(cls, val: Any) -> str:
        if val is None:
            return ''
        if isinstance(val, Enum):
            return val.value
        if isinstance(val, (list, tuple)):
            return ','.join(cls._as_str(v) for v in val)
        return str(val)
