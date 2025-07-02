from __future__ import annotations

import math
import re
from dataclasses import dataclass
from decimal import Decimal
from typing import TYPE_CHECKING, Generic, TypeVar, Union


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


T = TypeVar("T")


@dataclass
class SemicolonSeparatedList(Generic[T]):
    element: list[T]

    def __str__(self) -> str:
        return ";".join(str(t) for t in self.element)


@dataclass
class TimeBezierPoint:
    x1: Number
    y1: Number
    x2: Number
    y2: Number

    def __post_init__(self) -> None:
        assert self.x1 >= 0 and self.x1 <= 1
        assert self.y1 >= 0 and self.y1 <= 1
        assert self.x2 >= 0 and self.x2 <= 1
        assert self.y2 >= 0 and self.y2 <= 1

    def __str__(self) -> str:
        return f"{self.x1} {self.y1} {self.x2} {self.y2}"


@dataclass
class ClockValue:
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/Content_type#clock-value
    """

    seconds: Number
    minutes: int = 0
    hours: int = 0

    def __post_init__(self):
        assert self.seconds >= 0
        assert self.minutes >= 0 and self.minutes < 60
        assert self.hours >= 0

    @staticmethod
    def from_str(clock_str: str) -> "ClockValue":
        """
        Parses the string representation of a clock value and returns the equivalent ClockValue object
        """
        clock_str = clock_str.strip()
        # Full Clock Value: hours:minutes:seconds.fractional seconds
        full_clock_value = re.fullmatch(
            r"(\d+):([0-5]\d):([0-5]\d(?:\.\d+)?)", clock_str
        )
        if full_clock_value is not None:
            hours = int(full_clock_value.group(1))
            minutes = int(full_clock_value.group(2))
            seconds = float(full_clock_value.group(3))
            return ClockValue(seconds, minutes, hours)

        # Partial Clock Value:  minutes:seconds.fractional seconds
        partial_clock_value = re.fullmatch(r"([0-5]\d):([0-5]\d(?:\.\d+)?)", clock_str)
        if partial_clock_value is not None:
            minutes = int(partial_clock_value.group(1))
            seconds = float(partial_clock_value.group(2))
            return ClockValue(seconds, minutes)

        # Timecount Value: Value Unit
        timecount_value = re.fullmatch(r"(\d+(?:\.\d+)?)(h|min|s|ms)?", clock_str)
        if timecount_value is not None:
            value = float(timecount_value.group(1))
            unit = timecount_value.group(2)

            hours = 0
            minutes = 0
            seconds = 0

            if unit is None or unit == "s":
                seconds = value
            elif unit == "ms":
                seconds = value / 1000
            elif unit == "min":
                seconds = value * 60
            elif unit == "h":
                seconds = value * 60 * 60

            if seconds >= 60:
                minutes = int(seconds // 60)
                seconds = seconds % 60
            if minutes >= 60:
                hours = minutes // 60
                minutes = minutes % 60

            return ClockValue(seconds, minutes, hours)
        raise Exception("Unknown Clock Value Format")

    def __str__(self) -> str:
        full_seconds = math.floor(self.seconds)
        partial_seconds = self.seconds - full_seconds
        if partial_seconds > 0:
            return (
                f"{self.hours}:{self.minutes:02}:{full_seconds:02}{partial_seconds:.6f}"
            )
        return f"{self.hours}:{self.minutes:02}:{full_seconds:02}"

