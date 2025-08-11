from __future__ import annotations
from datetime import datetime

import math
from dataclasses import dataclass
from datetime import timedelta
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


# https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/begin
# https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/end

@dataclass
class SyncbaseValue:
    element_id: str
    event: Literal["begin", "end"]
    offset: timedelta | None

    def __str__(self) -> str:
        str_value = f"{self.element_id}.{self.event}"
        if self.offset is not None:
            offset_str = to_clock_value(self.offset)
            if not offset_str.startswith("-"):
                offset_str = "+" + offset_str
            str_value += offset_str
        return str_value


@dataclass
class EventValue:
    element_id: str | None
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
    offset: timedelta | None

    def __str__(self) -> str:
        str_value = ""
        if self.element_id is not None:
            str_value= f"{self.element_id}."
        str_value += f"{self.event}"
        if self.offset is not None:
            offset_str = to_clock_value(self.offset)
            if not offset_str.startswith("-"):
                offset_str = "+" + offset_str
            str_value += offset_str
        return str_value


@dataclass
class RepeatValue:
    element_id: str | None
    repeat_number: int
    offset: timedelta | None

    def __str__(self) -> str:
        str_value = ""
        if self.element_id is not None:
            str_value = f"{self.element_id}."
        str_value+= f"repeat({self.repeat_number})"

        if self.offset is not None:
            offset_str = to_clock_value(self.offset)
            if not offset_str.startswith("-"):
                offset_str = "+" + offset_str
            str_value += offset_str
        return str_value


@dataclass
class AccessKeyValue:
    key: str
    offset: timedelta | None

    def __str__(self) -> str:
        str_value = f"accessKey({self.key})"
        if self.offset is not None:
            offset_str = to_clock_value(self.offset)
            if not offset_str.startswith("-"):
                offset_str = "+" + offset_str
            str_value += offset_str
        return str_value


AnimationTimingEvent = Union[
    timedelta,
    SyncbaseValue,
    EventValue,
    RepeatValue,
    AccessKeyValue,
    datetime,
    'Literal["indefinite"]'
]


def to_clock_value(delta: timedelta) -> str:
    """Format timedelta as ClockValue SVG type.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/Content_type#clock-value
    https://svgwg.org/specs/animations/#ClockValueSyntax
    """
    seconds = delta.total_seconds()

    sign = ""
    if seconds < 0:
        sign = "-"
        seconds = abs(seconds)

    partial_seconds = seconds - math.floor(seconds)
    seconds = int(seconds)
    fraction = ""
    if partial_seconds > 0:
        fraction = f"{partial_seconds:.6f}".strip("0")

    # Format as Timecount-val.
    if abs(seconds) < 60:
        # The "s" suffix is optional but it's good for readability:
        # in JS, time is represented in miliseconds, so
        # just a number without a suffix may confuse JS engineers.
        return f"{sign}{seconds}{fraction}s"

    # Format as Full-clock-val.
    minutes, full_seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{sign}{hours}:{minutes:02}:{full_seconds:02}{fraction}"


def to_wallclock_sync_value(time: datetime) -> str:
    iso_time = time.isoformat(" ")
    return f"wallclock({iso_time})"
