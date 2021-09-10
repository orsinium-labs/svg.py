from pathlib import Path
import pytest
import examples
import svg


@pytest.mark.parametrize('name', examples.__all__)
def test_examples_up_to_date(name: str) -> None:
    module = getattr(examples, name)
    root_element = module.draw()
    assert isinstance(root_element, svg.SVG)

    out_path = Path(__file__).parent.parent / 'examples' / f'{name}.svg'
    expected = out_path.read_text()
    assert str(root_element) == expected.strip()
