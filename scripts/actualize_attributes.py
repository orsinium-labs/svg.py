import re
from pathlib import Path
from typing import Iterator

POJECT_ROOT = Path(__file__).parent.parent.absolute()


REX_ATTR = re.compile(re.escape('>{{SVGAttr("') + '([a-zA-Z-]+)' + re.escape('")}}</'))


def get_attrs(path: Path) -> Iterator[str]:
    path /= 'index.html'
    if not path.is_file():
        return
    content = path.read_text()
    for match in REX_ATTR.finditer(content):
        yield match.group(1)


def run() -> None:
    mdn_root = POJECT_ROOT.parent / 'mdn-source'
    svg_ref_root = mdn_root / 'files' / 'en-us' / 'web' / 'svg'

    out_path = POJECT_ROOT / 'tests' / 'fixtures' / 'attrs.txt'
    with out_path.open('w') as out_stream:
        for ref_path in (svg_ref_root / 'element').iterdir():
            for attr in get_attrs(ref_path):
                print(f'{ref_path.name}.{attr}', file=out_stream)


if __name__ == '__main__':
    run()
