"""
Tutorial:
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform

Usage:
    PYTHONPATH=. python3 examples/transform.py > examples/transform.svg
    xdg-open examples/transform.svg

We use functions instead of <g> and <use>
because it gives a better control over types.
"""
from typing import List
import svg


def heart_path() -> List[svg.PathData]:
    return [
        svg.M(10, 30),
        svg.Arc(20, 20, 0, False, True, x=50, y=30),
        svg.Arc(20, 20, 0, False, True, x=90, y=30),
        svg.Q(90, 60, 50, 90),
        svg.Q(10, 60, 10, 30),
        svg.Z(),
    ]


def draw() -> svg.SVG:
    return svg.SVG(
        viewBox=svg.ViewBoxSpec(-40, 0, 150, 100),
        xmlns="http://www.w3.org/2000/svg",

        elements=[
            svg.Path(
                d=heart_path(),
                fill="grey",
                transform=[
                    svg.Rotate(-10, 50, 100),
                    svg.Translate(-36, 45.5),
                    svg.SkewX(40),
                    svg.Scale(1, 0.5),
                ],
            ),
            svg.Path(
                d=heart_path(),
                fill="none",
                stroke="red",
            ),
        ],
    )


if __name__ == '__main__':
    print(draw())
