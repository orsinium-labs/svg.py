from __future__ import annotations
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
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#moveto_path_commands
    """
    command = 'M'
    x: Number
    y: Number


@dataclass
class MoveToRel(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#moveto_path_commands
    """
    command = 'm'
    dx: Number
    dy: Number


@dataclass
class LineTo(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#lineto_path_commands
    """
    command = 'L'
    x: Number
    y: Number


@dataclass
class LineToRel(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#lineto_path_commands
    """
    command = 'l'
    dx: Number
    dy: Number


@dataclass
class HorizontalLineTo(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#lineto_path_commands
    """
    command = 'H'
    x: Number


@dataclass
class HorizontalLineToRel(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#lineto_path_commands
    """
    command = 'h'
    dx: Number


@dataclass
class VerticalLineTo(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#lineto_path_commands
    """
    command = 'V'
    y: Number


@dataclass
class VerticalLineToRel(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#lineto_path_commands
    """
    command = 'v'
    dy: Number


@dataclass
class CubicBezier(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#cubic_b%C3%A9zier_curve
    """
    command = 'C'
    x1: Number
    y1: Number
    x2: Number
    y2: Number
    x: Number
    y: Number


@dataclass
class CubicBezierRel(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#cubic_b%C3%A9zier_curve
    """
    command = 'c'
    dx1: Number
    dy1: Number
    dx2: Number
    dy2: Number
    dx: Number
    dy: Number


@dataclass
class SmoothCubicBezier(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#cubic_b%C3%A9zier_curve
    """
    command = 'S'
    x2: Number
    y2: Number
    x: Number
    y: Number


@dataclass
class SmoothCubicBezierRel(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#cubic_b%C3%A9zier_curve
    """
    command = 's'
    dx2: Number
    dy2: Number
    dx: Number
    dy: Number


@dataclass
class QuadraticBezier(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#quadratic_b%C3%A9zier_curve
    """
    command = 'Q'
    x1: Number
    y1: Number
    x: Number
    y: Number


@dataclass
class QuadraticBezierRel(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#quadratic_b%C3%A9zier_curve
    """
    command = 'q'
    dx1: Number
    dy1: Number
    dx: Number
    dy: Number


@dataclass
class SmoothQuadraticBezier(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#quadratic_b%C3%A9zier_curve
    """
    command = 'T'
    x: Number
    y: Number


@dataclass
class SmoothQuadraticBezierRel(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#quadratic_b%C3%A9zier_curve
    """
    command = 't'
    dx: Number
    dy: Number


@dataclass
class Arc(PathData):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#elliptical_arc_curve
    """
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
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#elliptical_arc_curve
    """
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
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d#closepath
    """
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
