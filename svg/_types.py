from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import TYPE_CHECKING, Union


if TYPE_CHECKING:
    from typing_extensions import Literal


Number = Union[Decimal, float, int]


@dataclass
class Length:
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Content_type#length
    """
    value: Number
    unit: Literal["em", "ex", "px", "pt", "pc", "cm", "mm", "in", "%"]

    def __add__(self, other: Union[Length, Number]) -> Length:
        if isinstance(other, Length):
            if self.unit != other.unit:
                raise ValueError(f"Cannot add Lengths with different units: {self.unit} != {other.unit}")
            return Length(self.value + other.value, self.unit) # type: ignore
        elif isinstance(other, (int, float, Decimal)):
            return Length(self.value + other, self.unit) # type: ignore
        return NotImplemented

    def __radd__(self, other: Number) -> Length:
        return self + other

    def __sub__(self, other: Union[Length, Number]) -> Length:
        if isinstance(other, Length):
            if self.unit != other.unit:
                raise ValueError("Cannot subtract Lengths with different units")
            return Length(self.value - other.value, self.unit) # type: ignore
        elif isinstance(other, (int, float, Decimal)):
            return Length(self.value - other, self.unit) # type: ignore
        return NotImplemented

    def __rsub__(self, other: Number) -> Length:
        return Length(other - self.value, self.unit) # type: ignore

    def __mul__(self, other: Number) -> Length:
        if isinstance(other, (int, float, Decimal)):
            return Length(self.value * other, self.unit) # type: ignore
        return NotImplemented

    def __rmul__(self, other: Number) -> Length:
        return self * other

    def __truediv__(self, other: Number) -> Length:
        if isinstance(other, (int, float, Decimal)):
            return Length(self.value / other, self.unit) # type: ignore
        return NotImplemented

    def __neg__(self) -> Length:
        return Length(-self.value, self.unit)

    def __str__(self) -> str:
        return f"{self.value}{self.unit}"


@dataclass
class PreserveAspectRatio:
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/preserveAspectRatio
    """
    alignment: Literal[
        "none",
        "xMinYMin",
        "xMidYMin",
        "xMaxYMin",
        "xMinYMid",
        "xMidYMid",
        "xMaxYMid",
        "xMinYMax",
        "xMidYMax",
        "xMaxYMax",
    ] = "xMidYMid"
    scale_type: Literal["meet", "slice"] = "meet"

    def __str__(self) -> str:
        return f"{self.alignment} {self.scale_type}"


@dataclass
class ViewBoxSpec:
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/viewBox
    """
    min_x: Number
    min_y: Number
    width: Number
    height: Number

    def __str__(self) -> str:
        return f"{self.min_x} {self.min_y} {self.width} {self.height}"
