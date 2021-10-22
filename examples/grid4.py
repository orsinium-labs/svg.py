"""
Tutorial:
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform

Usage:
    PYTHONPATH=. python3 examples/transform.py > examples/transform.svg
    xdg-open examples/transform.svg

We use functions instead of <g> and <use>
because it gives a better control over types.
"""
import svg


STROKE_LEN = 10
GAP = 10
WIDTH = 400
HEIGHT = 400

SHIFT = int(STROKE_LEN / 2)
STEP = STROKE_LEN + GAP


def make_cross(x: int, y: int) -> svg.Path:
    return svg.Path(
        stroke="#2c3e50",
        stroke_width=1,
        stroke_linecap="round",
        d=[
            # horizontal line
            svg.M(x - SHIFT, y),
            svg.L(x + SHIFT, y),
            # vertical line
            svg.M(x, y - SHIFT),
            svg.L(x, y + SHIFT),
        ],
    )


def draw() -> svg.SVG:
    canvas = svg.SVG(
        viewBox=svg.ViewBoxSpec(0, 0, WIDTH, HEIGHT),
        xmlns="http://www.w3.org/2000/svg",
        elements=[],
    )
    assert canvas.elements is not None
    for x in range(STROKE_LEN, WIDTH, STEP):
        for y in range(STROKE_LEN, HEIGHT, STEP):
            canvas.elements.append(make_cross(x=x, y=y))
    return canvas


if __name__ == '__main__':
    print(draw())
