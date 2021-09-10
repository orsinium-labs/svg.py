"""
Tutorial:
    https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Basic_Shapes

Usage:
    python3 examples/shapes.py > examples/shapes.svg
    xdg-open examples/shapes.svg
"""
import svg


def draw() -> svg.SVG:
    return svg.SVG(
        width=200,
        height=250,
        xmlns="http://www.w3.org/2000/svg",

        elements=[
            svg.Rect(
                x=10, y=10,
                width=30, height=30,
                stroke="black",
                fill="transparent",
                stroke_width=5,
            ),
            svg.Rect(
                x=60, y=10,
                rx=10, ry=10,
                width=30, height=30,
                stroke="black",
                fill="transparent",
                stroke_width=5,
            ),
            svg.Circle(
                cx=25, cy=75, r=20,
                stroke="red",
                fill="transparent",
                stroke_width=5,
            ),
            svg.Ellipse(
                cx=75, cy=75,
                rx=20, ry=5,
                stroke="red",
                fill="transparent",
                stroke_width=5,
            ),
            svg.Line(
                x1=10, x2=50,
                y1=110, y2=150,
                stroke="orange",
                stroke_width=5,
            ),
            svg.Polyline(
                points=[
                    60, 110, 65, 120, 70, 115, 75, 130, 80,
                    125, 85, 140, 90, 135, 95, 150, 100, 145,
                ],
                stroke="orange",
                fill="transparent",
                stroke_width=5,
            ),
            svg.Polygon(
                points=[
                    50, 160, 55, 180, 70, 180, 60, 190, 65, 205,
                    50, 195, 35, 205, 40, 190, 30, 180, 45, 180,
                ],
                stroke="green",
                fill="transparent",
                stroke_width=5,
            ),
            svg.Path(
                d=[
                    svg.M(20, 230),
                    svg.Q(40, 205, 50, 230),
                    svg.T(90, 230),
                ],
                fill="none",
                stroke="blue",
                stroke_width=5,
            ),
        ],
    )


if __name__ == '__main__':
    print(draw())
