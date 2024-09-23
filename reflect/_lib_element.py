from __future__ import annotations

from dataclasses import dataclass, fields

import svg


try:
    from functools import cached_property
except ImportError:
    cached_property = property  # type: ignore


@dataclass
class LibElement:
    title: str
    fields: list[str]

    @classmethod
    def parse_all(cls) -> list[LibElement]:
        result = []
        for el in svg.Element.__subclasses__():
            result.append(cls(
                title=el.element_name,
                fields=[f.name for f in fields(el)]
            ))
        return result

    @cached_property
    def attrs(self) -> set[str]:
        result = set()
        for field in self.fields:
            if field == 'elements':
                continue
            field = field.rstrip('_')
            field = field.replace('__', ':')
            field = field.replace('_', '-')
            result.add(field)
        return result
