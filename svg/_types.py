from __future__ import annotations

import math
import re
from dataclasses import dataclass
from decimal import Decimal
from typing import TYPE_CHECKING, Optional, Union, List


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


# https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/begin
# https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/end

@dataclass
class OffsetValue:
    sign: Literal["+", "-"]
    offset: ClockValue

    def __str__(self) -> str:
        return f"{self.sign}{self.offset}"


@dataclass
class SyncbaseValue:
    element_id: str
    event: Literal["begin", "end"]
    offset: Optional[OffsetValue]

    def __str__(self) -> str:
        str_value = f"{self.element_id}.{self.event}"
        if self.offset is not None:
            str_value += str(self.offset)
        return str_value


@dataclass
class EventValue:
    element_id: str
    event: Literal[
        "focus",
        "blur",
        "focusin",
        "focusout",
        "DOMActivate",
        "auxclick",
        "click",
        "dblclick",
        "mousedown",
        "mouseenter",
        "mouseleave",
        "mousemove",
        "mouseout",
        "mouseover",
        "mouseup",
        "wheel",
        "beforeinput",
        "input",
        "keydown",
        "keyup",
        "compositionstart",
        "compositionupdate",
        "compositionend",
        "load",
        "unload",
        "abort",
        "error",
        "select",
        "resize",
        "scroll",
        "beginEvent",
        "endEvent",
        "repeatEvent",
    ]
    offset: Optional[OffsetValue]

    def __str__(self) -> str:
        str_value = f"{self.element_id}.{self.event}"
        if self.offset is not None:
            str_value += str(self.offset)
        return str_value


@dataclass
class RepeatValue:
    element_id: str
    repeat_number: int
    offset: Optional[OffsetValue]

    def __str__(self) -> str:
        str_value = f"{self.element_id}.repeat({self.repeat_number})"
        if self.offset is not None:
            str_value += str(self.offset)
        return str_value


@dataclass
class AccessKeyValue:
    key: str
    offset: Optional[OffsetValue]

    def __str__(self) -> str:
        str_value = f'accessKey("{self.key}")'
        if self.offset is not None:
            str_value += str(self.offset)
        return str_value


from datetime import datetime

class WallclockSyncValue:
    time: datetime

    def __str__(self) -> str:
        return f"wallclock({self.time.isoformat(" ")})"


AnimationTimingEvent = Union[
    ClockValue,
    OffsetValue,
    SyncbaseValue,
    EventValue,
    RepeatValue,
    AccessKeyValue,
    WallclockSyncValue,
    Literal["indefinite"]
]

@dataclass
class SemicolonSeperatedList[T]:
    element: List[T] = []

    def __str__(self) -> str:
        return ";".join([str(t) for t in self.element])
