import re
from pathlib import Path
from typing import Iterator

POJECT_ROOT = Path(__file__).parent.parent.absolute()
REX_ATTR = re.compile(re.escape('{{SVGAttr("') + '([a-zA-Z-]+)' + re.escape('")}}'))


def get_attrs(path: Path) -> Iterator[str]:
    path /= 'index.html'
    assert path.is_file()
    content = path.read_text()
    for match in REX_ATTR.finditer(content):
        attr = match.group(1)
        ref_path = path.parent / attr / 'index.html'
        if not ref_path.is_file():
            continue
        yield attr


def run() -> None:
    mdn_root = POJECT_ROOT.parent / 'mdn-source'
    svg_ref_root = mdn_root / 'files' / 'en-us' / 'web' / 'svg'
    out_path = POJECT_ROOT / 'tests' / 'fixtures' / 'all_attrs.txt'
    with out_path.open('w') as out_stream:
        attrs = sorted(set(get_attrs(svg_ref_root / 'attribute')))
        for attr in attrs:
            print(attr, file=out_stream)


if __name__ == '__main__':
    run()
