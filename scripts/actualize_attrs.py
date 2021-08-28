import re
from pathlib import Path
from typing import Iterator

POJECT_ROOT = Path(__file__).parent.parent.absolute()


REX_TITLE = re.compile(r'title:\s<([a-zA-Z-]+)>')
REX_ATTR = re.compile(re.escape('>{{SVGAttr("') + '([a-zA-Z-]+)' + re.escape('")}}</'))


def get_attrs(path: Path) -> Iterator[str]:
    path /= 'index.html'
    if not path.is_file():
        return
    content = path.read_text()
    match = REX_TITLE.search(content)
    assert match, f'title not found for {path}'
    title = match.group(1)
    for match in REX_ATTR.finditer(content):
        attr = match.group(1)
        yield f'{title}.{attr}'


def run() -> None:
    mdn_root = POJECT_ROOT.parent / 'mdn-source'
    svg_ref_root = mdn_root / 'files' / 'en-us' / 'web' / 'svg'

    out_path = POJECT_ROOT / 'tests' / 'fixtures' / 'attrs.txt'
    with out_path.open('w') as out_stream:
        for ref_path in (svg_ref_root / 'element').iterdir():
            for attr in get_attrs(ref_path):
                print(attr, file=out_stream)


if __name__ == '__main__':
    run()
