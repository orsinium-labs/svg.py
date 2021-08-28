
from dataclasses import fields
from typing import Set
from pathlib import Path
import pytest

import svg
from svg._mixins import AttrsMixin


FIXTURES = Path(__file__).parent / 'fixtures'
DEPRECATED = (FIXTURES / 'deprecated.txt').read_text().split()


def get_attrs(cls) -> Set[str]:
    result = set()
    for field in fields(cls):
        key = field.name
        if key == 'elements':
            continue
        key = key.rstrip('_')
        key = key.replace('__', ':')
        key = key.replace('_', '-')
        result.add(key)
    return result


@pytest.mark.parametrize('cls', AttrsMixin.__subclasses__())
@pytest.mark.parametrize('name', DEPRECATED)
def test_no_deprecated__mixins(cls: AttrsMixin, name: str):
    name = name.replace('_colon_', ':')
    attrs = get_attrs(cls)
    assert name not in attrs


@pytest.mark.parametrize('cls', svg.elements.Element.__subclasses__())
@pytest.mark.parametrize('name', DEPRECATED)
def test_no_deprecated__elements(cls: svg.elements.Element, name: str):
    name = name.replace('_colon_', ':')
    attrs = get_attrs(cls)
    assert name not in attrs, name.replace('-', '_')
