from typing import List
import svg


STROKE_LEN = 10
GAP = 10
WIDTH = 400
HEIGHT = 400

SHIFT = int(STROKE_LEN / 2)
STEP = STROKE_LEN + GAP


def draw() -> svg.SVG:
    elements: List[svg.Element] = []
    do_shift = True
    for y in range(STROKE_LEN, HEIGHT, STEP):
        do_shift = not do_shift
        start_x = STROKE_LEN
        if do_shift:
            start_x += STROKE_LEN
        for x in range(start_x, WIDTH, STEP):
            for angle in (0, 60, -60):
                elements.append(svg.Path(
                    stroke="#2c3e50",
                    stroke_width=1,
                    stroke_linecap="round",
                    transform=[svg.Rotate(angle, x, y)],
                    d=[
                        svg.M(x - SHIFT, y),
                        svg.L(x + SHIFT, y),
                    ],
                ))
    return svg.SVG(
        viewBox=svg.ViewBoxSpec(0, 0, WIDTH, HEIGHT),
        xmlns="http://www.w3.org/2000/svg",
        elements=elements,
    )


if __name__ == '__main__':
    print(draw())
