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
    content: str
    status: list[str] | None = None
    spec_urls: list[str] | None = None
    browser_compat: object | None = None
    sidebar: object | None = None

    @classmethod
    def parse(cls, path: Path) -> MDNAttr | None:
        path /= 'index.md'
        if not path.is_file():
            return None
        raw = path.read_text()
        front_matter, _, markdown = raw.partition('\n---\n')
        fields: dict = next(yaml.load_all(front_matter, Loader=yaml.SafeLoader))
        page_type = fields.pop('page-type')
        assert page_type == 'svg-attribute'
        fields = {k.replace('-', '_'): v for k, v in fields.items()}
        return cls(**fields, content=markdown)

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
        if self.status and 'deprecated' in self.status:
            return True
        if '{{deprecated_header}}' in self.content.lower():
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
