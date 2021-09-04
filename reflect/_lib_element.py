from dataclasses import dataclass, fields
from functools import cached_property
from typing import List, Set

import svg


@dataclass
class LibElement:
    title: str
    fields: List[str]

    @classmethod
    def parse_all(cls) -> List['LibElement']:
        result = []
        for el in svg.Element.__subclasses__():
            result.append(cls(
                title=el.element_name,
                fields=[f.name for f in fields(el)]
            ))
        return result

    @cached_property
    def attrs(self) -> Set[str]:
        result = set()
        for field in self.fields:
            if field == 'elements':
                continue
            field = field.rstrip('_')
            field = field.replace('__', ':')
            field = field.replace('_', '-')
            result.add(field)
        return result
