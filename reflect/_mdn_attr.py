from __future__ import annotations
import re
from dataclasses import dataclass
from pathlib import Path

import yaml


try:
    from functools import cached_property
except ImportError:
    cached_property = property  # type: ignore


REX_EL = re.compile(r'li>\{\{\s*SVGElement\(["\']([a-zA-Z-]+)["\']\)\s*\}\}\.?</')
DEPRECATED = [
    # attributes of <font-face> which is deprecated
    'underline-thickness',
    'underline-position',
    'overline-thickness',
    'overline-position',
    'strikethrough-thickness',
    'strikethrough-position',

    # not supported by any browser
    'crossorigin',
    'systemLanguage',
]


@dataclass
class MDNAttr:
    title: str
    slug: str
    tags: list[str]
    content: str
    spec_urls: list[str]

    @classmethod
    def parse(cls, path: Path) -> MDNAttr | None:
        path /= 'index.md'
        if not path.is_file():
            return None
        raw = path.read_text()
        first, _, second = raw.partition('\n---\n')
        fields: dict = next(yaml.load_all(first, Loader=yaml.SafeLoader))
        fields.pop('browser-compat', None)
        spec_urls = fields.pop('spec-urls', [])
        return cls(**fields, content=second, spec_urls=spec_urls)

    @classmethod
    def parse_all(cls, path: Path) -> list[MDNAttr]:
        result = []
        for subpath in (path / 'attribute').iterdir():
            attr = cls.parse(subpath)
            if attr is not None:
                result.append(attr)
        return result

    @cached_property
    def is_deprecated(self) -> bool:
        if self.title in DEPRECATED:
            return True
        if 'Deprecated' in self.tags:
            return True
        if '<div>{{SVGRef}}{{Deprecated_Header}}</div>' in self.content:
            return True
        if '<div>{{SVGRef}}{{deprecated_header}}</div>' in self.content:
            return True
        if '<div>{{deprecated_header}}</div>' in self.content:
            return True
        return False

    @cached_property
    def elements(self) -> set[str]:
        sep = 'You can use this attribute with the following SVG elements:'
        _, _, txt = self.content.partition(sep)
        txt, _, _ = self.content.partition('</ul>')
        txt, _, _ = self.content.partition('See also')
        result = set()
        for match in REX_EL.finditer(txt):
            result.add(match.group(1))
        return result
