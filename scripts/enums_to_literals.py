import re
from pathlib import Path


LIB_PATH = Path(__file__).parent.parent / 'svg'
REX_VAL = re.compile(r'"[a-zA-Z0-9-]+"')


def parse_enums():
    content = (LIB_PATH / 'enums.py').read_text()
    parts = content.split('\nclass ')
    for part in parts:
        enum_name = part.split("(", maxsplit=1)[0]
        values = REX_VAL.findall(part)
        literal = 'Literal[' + ','.join(values) + ']'
        yield enum_name, literal


def fix(path: Path):
    content = path.read_text()
    for enum_name, literal in parse_enums():
        content = content.replace(f'enums.{enum_name}', literal)
    path.write_text(content)


def run() -> None:
    for path in LIB_PATH.iterdir():
        if not path.name.endswith('.py'):
            continue
        fix(path)


if __name__ == '__main__':
    run()
