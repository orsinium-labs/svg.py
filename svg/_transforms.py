from dataclasses import dataclass
from typing import Optional


class Transform:
    pass


@dataclass
class Matrix(Transform):
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int

    def __str__(self):
        return f'matrix({self.a} {self.b} {self.c} {self.d} {self.e} {self.f})'


@dataclass
class Translate(Transform):
    x: int
    y: Optional[int] = None

    def __str__(self):
        if self.y is None:
            return f'translate({self.x})'
        return f'translate({self.x} {self.y})'


@dataclass
class Scale(Transform):
    x: int
    y: Optional[int] = None

    def __str__(self):
        if self.y is None:
            return f'scale({self.x})'
        return f'scale({self.x} {self.y})'


@dataclass
class Rotate(Transform):
    a: int
    x: Optional[int] = None
    y: Optional[int] = None

    def __str__(self):
        if self.x is None:
            return f'rotate({self.a})'
        assert self.y
        return f'rotate({self.a} {self.x} {self.y})'


@dataclass
class SkewX(Transform):
    a: int

    def __str__(self):
        return f'skewX({self.a})'


@dataclass
class SkewY(Transform):
    a: int

    def __str__(self):
        return f'skewY({self.a})'
