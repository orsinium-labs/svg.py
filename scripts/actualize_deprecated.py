from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.absolute()


def get_attrs_ref_root() -> Path:
    mdn_root = PROJECT_ROOT.parent / 'mdn-source'
    svg_ref_root = mdn_root / 'files' / 'en-us' / 'web' / 'svg'
    return svg_ref_root / 'attribute'


def is_deprecated(path: Path) -> bool:
    path /= 'index.html'
    if not path.is_file():
        return False
    content = path.read_text()
    return '{{Deprecated_Header}}' in content


def run() -> None:
    out_path = PROJECT_ROOT / 'tests' / 'fixtures' / 'deprecated.txt'
    with out_path.open('w') as out_stream:
        for ref_path in get_attrs_ref_root().iterdir():
            if is_deprecated(ref_path):
                print(ref_path.name, file=out_stream)


if __name__ == '__main__':
    run()
