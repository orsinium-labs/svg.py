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

**Try svg.py online:** [svg.orsinium.dev](https://svg.orsinium.dev/).

```python
import svg
canvas = svg.SVG(
    width=60,
    height=60,
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

## Projects using svg.py

The github topic [svg-py](https://github.com/topics/svg-py) contains some of the projects that use svg.py in one way or another. If you want your project to appear on the list, simply add `svg-py` into the list of project topics. [Here is how][add-topic].

[add-topic]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics#adding-topics-to-your-repository
