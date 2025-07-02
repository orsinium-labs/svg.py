from pathlib import Path

import pytest

import reflect


LIB_ELEMENTS = reflect.LibElement.parse_all()
ROOT = Path(__file__).parent.parent.parent
MDN_ROOT = ROOT / 'mdn-source' / 'files' / 'en-us' / 'web' / 'svg' / 'reference'
# If the line below fails, run the following one directory up the root of svg.py:
#   git clone https://github.com/mdn/content.git mdn-source --depth 1
assert MDN_ROOT.is_dir(), f'you must clone mdn-source into {MDN_ROOT} before you can run tests'
MDN_ATTRS = reflect.MDNAttr.parse_all(MDN_ROOT)

FIXTURES = Path(__file__).parent / 'fixtures'
DEPRECATED = (FIXTURES / 'deprecated_attrs.txt').read_text().split()

assert LIB_ELEMENTS
assert MDN_ATTRS


@pytest.mark.parametrize('lib_element', LIB_ELEMENTS)
@pytest.mark.parametrize('mdn_attr', MDN_ATTRS)
def test_attrs(lib_element: reflect.LibElement, mdn_attr: reflect.MDNAttr):
    if mdn_attr.is_deprecated:
        msg = f'attr `{mdn_attr.title}` is deprecated but is set for `{lib_element.title}`'
        assert mdn_attr.title not in lib_element.attrs, msg
        return
    if mdn_attr.title in DEPRECATED:
        msg = f'attr `{mdn_attr.title}` is deprecated but is set for `{lib_element.title}`'
        assert mdn_attr.title not in lib_element.attrs, msg
        return

    if lib_element.title in mdn_attr.elements:
        msg = f'attr `{mdn_attr.title}` should be set for `{lib_element.title}` but it is not'
        assert mdn_attr.title in lib_element.attrs, msg

    # <g> and <use> may have additional undocumented attributes
    if lib_element.title in {'g', 'use'}:
        return
    if mdn_attr.elements and lib_element.title not in mdn_attr.elements:
        msg = f'attr `{mdn_attr.title}` should not be set for `{lib_element.title}` but it is'
        assert mdn_attr.title not in lib_element.attrs, msg
