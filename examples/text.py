"""
Tutorial:
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/text

Usage:
    python3 examples/text.py > examples/text.svg
    chromium examples/text.svg
"""
from textwrap import dedent

import svg


def draw() -> svg.SVG:
    return svg.SVG(
        width=240,
        height=80,
        elements=[
            svg.Style(
                text=dedent("""
                    .small { font: italic 13px sans-serif; }
                    .heavy { font: bold 30px sans-serif; }

                    /* Note that the color of the text is set with the    *
                    * fill property, the color property is for HTML only */
                    .Rrrrr { font: italic 40px serif; fill: red; }
                """),
            ),
            svg.Text(x=20, y=35, class_=["small"], text="My"),
            svg.Text(x=40, y=35, class_=["heavy"], text="cat"),
            svg.Text(x=55, y=55, class_=["small"], text="is"),
            svg.Text(x=65, y=55, class_=["Rrrrr"], text="Grumpy!"),
        ],
    )


if __name__ == '__main__':
    print(draw())
