"""
Tutorial:
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/animate

Usage:
    python3 examples/animate.py > examples/animate.svg
    xdg-open examples/animate.svg
"""
import svg


def draw() -> svg.SVG:
    return svg.SVG(
        x=0, y=0,
        width=10, height=10,
        elements=[svg.Rect(x=0, y=0,
                           width=10, height=10,
                           elements=[svg.Animate(
                               attributeName="rx",
                               values="0;5;0",
                               dur="10s",
                               repeatCount="indefinite")]
                           )]
    )


if __name__ == '__main__':
    print(draw())
