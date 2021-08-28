
from dataclasses import fields
from typing import Set, Type
from pathlib import Path
import pytest

import svg
from svg._mixins import AttrsMixin


FIXTURES = Path(__file__).parent / 'fixtures'
DEPRECATED = (FIXTURES / 'deprecated_attrs.txt').read_text().split()
ALL = (FIXTURES / 'attrs.txt').read_text().split()


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


def get_element(name) -> Type[svg.elements.Element]:
    for el in svg.elements.Element.__subclasses__():
        if el.element_name == name:
            return el
    pytest.skip()


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


@pytest.mark.parametrize('name', ALL)
def test_has_attr(name: str):
    if name.startswith('fe'):
        pytest.skip()
    el_name, attr_name = name.split('.')
    if attr_name in DEPRECATED:
        pytest.skip()
    element = get_element(el_name)
    attrs = get_attrs(element)
    assert attr_name in attrs
