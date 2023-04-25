from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from ._types import Number


class Transform:
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform
    """
    pass


@dataclass
class Matrix(Transform):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform#matrix
    """
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
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform#translate
    """
    x: Number
    y: Optional[Number] = None

    def __str__(self):
        if self.y is None:
            return f'translate({self.x})'
        return f'translate({self.x} {self.y})'


@dataclass
class Scale(Transform):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform#scale
    """
    x: Number
    y: Optional[Number] = None

    def __str__(self):
        if self.y is None:
            return f'scale({self.x})'
        return f'scale({self.x} {self.y})'


@dataclass
class Rotate(Transform):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform#rotate
    """
    a: Number
    x: Optional[Number] = None
    y: Optional[Number] = None

    def __str__(self):
        if self.x is None:
            return f'rotate({self.a})'
        assert self.y is not None
        return f'rotate({self.a} {self.x} {self.y})'


@dataclass
class SkewX(Transform):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform#skewx
    """
    a: Number

    def __str__(self):
        return f'skewX({self.a})'


@dataclass
class SkewY(Transform):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform#skewy
    """
    a: Number

    def __str__(self):
        return f'skewY({self.a})'
