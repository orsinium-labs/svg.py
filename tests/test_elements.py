
from pathlib import Path

import pytest

import svg


FIXTURES = Path(__file__).parent / 'fixtures'
DEPRECATED = (FIXTURES / 'deprecated_elements.txt').read_text().split()


@pytest.mark.parametrize('cls', svg.Element.__subclasses__())
@pytest.mark.parametrize('name', DEPRECATED)
def test_no_deprecated__elements(cls: svg.Element, name: str):
    assert cls.element_name != name
    assert cls.element_name.lower() != name.lower()


@pytest.mark.parametrize('cls', svg.Element.__subclasses__())
def test_element_exported(cls: svg.Element):
    assert cls in vars(svg).values()
