# svg.py

Python library to generate SVG files.

Features:

+ Compatible with all SVG standards: 1.1, 1.2, 2.0, Tiny.
+ 100% type safe.
+ Pure Python.
+ No third-party runtime dependencies.
+ No deprecated attributes, only what actually works.
+ The same names and structure as in the standard. If you know how to write SVG files, you know how to use this library.

Based on [svg-xsd-schema](https://github.com/dumistoklus/svg-xsd-schema/blob/master/svg.xsd) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/SVG).

## Installation

```bash
python3 -m pip install --user svg.py
```

## Usage

```python
import svg
canvas = svg.SVG(
    width=60,
    height=60,
    xmlns="http://www.w3.org/2000/svg",
    elements=[
        svg.Circle(
            cx=30, cy=30, r=20,
            stroke="red",
            fill="white",
            stroke_width=5,
        ),
    ],
)
print(canvas)
```

See [examples](./examples/) for more.
