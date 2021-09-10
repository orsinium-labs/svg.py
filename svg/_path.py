from dataclasses import astuple, dataclass
from typing import ClassVar

from ._types import Number


@dataclass
class PathData:
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d
    """
    command: ClassVar[str]

    def __str__(self) -> str:
        points = []
        for p in astuple(self):
            if isinstance(p, bool):
                p = int(p)
            points.append(str(p))
        joined = " ".join(points)
        return f"{self.command} {joined}"


@dataclass
class MoveTo(PathData):
    command = 'M'
    x: Number
    y: Number


@dataclass
class MoveToRel(PathData):
    command = 'm'
    dx: Number
    dy: Number


@dataclass
class LineTo(PathData):
    command = 'L'
    x: Number
    y: Number


@dataclass
class LineToRel(PathData):
    command = 'l'
    dx: Number
    dy: Number


@dataclass
class HorizontalLineTo(PathData):
    command = 'H'
    x: Number


@dataclass
class HorizontalLineToRel(PathData):
    command = 'h'
    dx: Number


@dataclass
class VerticalLineTo(PathData):
    command = 'V'
    y: Number


@dataclass
class VerticalLineToRel(PathData):
    command = 'v'
    dy: Number


@dataclass
class CubicBezier(PathData):
    command = 'C'
    x1: Number
    y1: Number
    x2: Number
    y2: Number
    x: Number
    y: Number


@dataclass
class CubicBezierRel(PathData):
    command = 'c'
    dx1: Number
    dy1: Number
    dx2: Number
    dy2: Number
    dx: Number
    dy: Number


@dataclass
class SmoothCubicBezier(PathData):
    command = 'S'
    x2: Number
    y2: Number
    x: Number
    y: Number


@dataclass
class SmoothCubicBezierRel(PathData):
    command = 's'
    dx2: Number
    dy2: Number
    dx: Number
    dy: Number


@dataclass
class QuadraticBezier(PathData):
    command = 'Q'
    x1: Number
    y1: Number
    x: Number
    y: Number


@dataclass
class QuadraticBezierRel(PathData):
    command = 'q'
    dx1: Number
    dy1: Number
    dx: Number
    dy: Number


@dataclass
class SmoothQuadraticBezier(PathData):
    command = 'T'
    x: Number
    y: Number


@dataclass
class SmoothQuadraticBezierRel(PathData):
    command = 't'
    dx: Number
    dy: Number


@dataclass
class Arc(PathData):
    command = 'A'
    rx: Number
    ry: Number
    angle: Number
    large_arc: bool
    sweep: bool
    x: Number
    y: Number


@dataclass
class ArcRel(PathData):
    command = 'a'
    rx: Number
    ry: Number
    angle: Number
    large_arc: bool
    sweep: bool
    dx: Number
    dy: Number


@dataclass
class ClosePath(PathData):
    command = 'Z'


# aliases
M = MoveTo
m = MoveToRel
L = LineTo
l = LineToRel  # noqa: E741
H = HorizontalLineTo
h = HorizontalLineToRel
V = VerticalLineTo
v = VerticalLineToRel
C = CubicBezier
c = CubicBezierRel
S = SmoothCubicBezier
s = SmoothCubicBezierRel
Q = QuadraticBezier
q = QuadraticBezierRel
T = SmoothQuadraticBezier
t = SmoothQuadraticBezierRel
A = Arc
a = ArcRel
Z = ClosePath
