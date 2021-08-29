import re
from pathlib import Path
from typing import Iterator

POJECT_ROOT = Path(__file__).parent.parent.absolute()


REX_TITLE = re.compile(r'title:\s\'?([a-zA-Z\-\:]+)\'?')
REX_EL = re.compile(re.escape('>{{SVGElement("') + '([a-zA-Z-]+)' + re.escape('")}}</'))


def get_elements(path: Path) -> Iterator[str]:
    path /= 'index.html'
    if not path.is_file():
        return
    content = path.read_text()
    match = REX_TITLE.search(content)
    assert match, f'title not found for {path}'
    title = match.group(1)
    content = content.split('</ul>', maxsplit=1)[0]
    for match in REX_EL.finditer(content):
        el = match.group(1)
        yield f'{title}.{el}'


def run() -> None:
    mdn_root = POJECT_ROOT.parent / 'mdn-source'
    svg_ref_root = mdn_root / 'files' / 'en-us' / 'web' / 'svg'

    out_path = POJECT_ROOT / 'tests' / 'fixtures' / 'elements.txt'
    with out_path.open('w') as out_stream:
        for ref_path in (svg_ref_root / 'attribute').iterdir():
            for el in get_elements(ref_path):
                print(el, file=out_stream)


if __name__ == '__main__':
    run()
