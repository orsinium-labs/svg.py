from pathlib import Path


POJECT_ROOT = Path(__file__).parent.parent.absolute()


def is_deprecated(path: Path) -> bool:
    path /= 'index.html'
    if not path.is_file():
        return False
    content = path.read_text()
    if '{{Deprecated_Header}}</div>' in content:
        return True
    if '{{deprecated_header}}</div>' in content:
        return True
    return False


def run() -> None:
    mdn_root = POJECT_ROOT.parent / 'mdn-source'
    svg_ref_root = mdn_root / 'files' / 'en-us' / 'web' / 'svg'

    out_path = POJECT_ROOT / 'tests' / 'fixtures' / 'deprecated_attrs.txt'
    with out_path.open('w') as out_stream:
        for ref_path in (svg_ref_root / 'attribute').iterdir():
            if is_deprecated(ref_path):
                print(ref_path.name, file=out_stream)

    out_path = POJECT_ROOT / 'tests' / 'fixtures' / 'deprecated_elements.txt'
    with out_path.open('w') as out_stream:
        for ref_path in (svg_ref_root / 'element').iterdir():
            if is_deprecated(ref_path):
                print(ref_path.name, file=out_stream)


if __name__ == '__main__':
    run()
