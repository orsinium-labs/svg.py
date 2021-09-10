from dataclasses import dataclass
from typing import Optional
from ._types import Number


class Transform:
    pass


@dataclass
class Matrix(Transform):
    a: Number
    b: Number
    c: Number
    d: Number
    e: Number
    f: Number

    def __str__(self):
        return f'matrix({self.a} {self.b} {self.c} {self.d} {self.e} {self.f})'


@dataclass
class Translate(Transform):
    x: Number
    y: Optional[Number] = None

    def __str__(self):
        if self.y is None:
            return f'translate({self.x})'
        return f'translate({self.x} {self.y})'


@dataclass
class Scale(Transform):
    x: Number
    y: Optional[Number] = None

    def __str__(self):
        if self.y is None:
            return f'scale({self.x})'
        return f'scale({self.x} {self.y})'


@dataclass
class Rotate(Transform):
    a: Number
    x: Optional[Number] = None
    y: Optional[Number] = None

    def __str__(self):
        if self.x is None:
            return f'rotate({self.a})'
        assert self.y
        return f'rotate({self.a} {self.x} {self.y})'


@dataclass
class SkewX(Transform):
    a: Number

    def __str__(self):
        return f'skewX({self.a})'


@dataclass
class SkewY(Transform):
    a: Number

    def __str__(self):
        return f'skewY({self.a})'
