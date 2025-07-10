"""
Tutorial:
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/animateTransform

Usage:
    python3 examples/animate_transform.py > examples/animate_transform.svg
    chromium examples/animate_transform.svg
"""
from datetime import timedelta
import svg


def draw() -> svg.SVG:
    return svg.SVG(
        x=0, y=0,
        width=120, height=120,
        elements=[svg.Polygon(
            points=[60, 30, 90, 90, 30, 90],
            elements=[svg.AnimateTransform(
                attributeName="transform",
                type="rotate",
                from_="0 60 70",
                to="360 60 70",
                dur=timedelta(seconds=10),
                repeatCount="indefinite",
            )]
        )]
    )


if __name__ == '__main__':
    print(draw())
