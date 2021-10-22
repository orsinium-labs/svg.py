import svg


STROKE_LEN = 10
GAP = 10
WIDTH = 400
HEIGHT = 400

SHIFT = int(STROKE_LEN / 2)
STEP = STROKE_LEN + GAP


def draw() -> svg.SVG:
    lines = []
    for x in range(STROKE_LEN, WIDTH, STEP):
        for y in range(STROKE_LEN, HEIGHT, STEP):
            lines.extend([
                # horizontal line
                svg.M(x - SHIFT, y),
                svg.L(x + SHIFT, y),
                # vertical line
                svg.M(x, y - SHIFT),
                svg.L(x, y + SHIFT),
            ])
    return svg.SVG(
        viewBox=svg.ViewBoxSpec(0, 0, WIDTH, HEIGHT),
        xmlns="http://www.w3.org/2000/svg",
        elements=[svg.Path(
            stroke="#2c3e50",
            stroke_width=1,
            stroke_linecap="round",
            d=lines,
        )],
    )


if __name__ == '__main__':
    print(draw())
