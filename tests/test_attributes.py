
from dataclasses import fields
from typing import Set, Type
from pathlib import Path
import pytest

import svg
from svg._mixins import AttrsMixin


FIXTURES = Path(__file__).parent / 'fixtures'
REF_DEPRECATED = (FIXTURES / 'deprecated_attrs.txt').read_text().split()
REF_BY_ELEMENT = (FIXTURES / 'attrs.txt').read_text().split()
REF_ALL = (FIXTURES / 'all_attrs.txt').read_text().split()

REF_DEPRECATED.extend([
    # attributes of <font-face> which is deprecated
    'underline-thickness',
    'underline-position',
    'overline-thickness',
    'overline-position',
    'strikethrough-thickness',
    'strikethrough-position',

    # not supported by any browser
    'crossorigin',
])


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


def get_all_attrs() -> Set[str]:
    result: Set[str] = set()
    for el in svg.elements.Element.__subclasses__():
        result.update(get_attrs(el))
    return result


@pytest.mark.parametrize('cls', AttrsMixin.__subclasses__())
@pytest.mark.parametrize('name', REF_DEPRECATED)
def test_no_deprecated__mixins(cls: AttrsMixin, name: str):
    name = name.replace('_colon_', ':')
    attrs = get_attrs(cls)
    assert name not in attrs
    assert name.lower() not in {attr.lower() for attr in attrs}


@pytest.mark.parametrize('cls', svg.elements.Element.__subclasses__())
@pytest.mark.parametrize('name', REF_DEPRECATED)
def test_no_deprecated__elements(cls: svg.elements.Element, name: str):
    name = name.replace('_colon_', ':')
    attrs = get_attrs(cls)
    assert name not in attrs, name.replace('-', '_')
    assert name.lower() not in {attr.lower() for attr in attrs}


@pytest.mark.parametrize('name', REF_BY_ELEMENT)
def test_element_has_attr(name: str):
    el_name, attr_name = name.split('.')
    if attr_name.lower() in REF_DEPRECATED:
        pytest.skip()
    element = get_element(el_name)
    attrs = get_attrs(element)
    assert attr_name in attrs


LIB_ALL = get_all_attrs()


@pytest.mark.parametrize('name', REF_ALL)
def test_attr_is_represented_at_least_once(name: str):
    if name.lower() in REF_DEPRECATED:
        pytest.skip()
    assert name in LIB_ALL
