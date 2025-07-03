from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import timedelta
from decimal import Decimal

from typing import TYPE_CHECKING, Generic, TypeVar, Union


Indefinite = str
if TYPE_CHECKING:
    from typing_extensions import Literal
    Indefinite = Literal["indefinite"]


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
                offset_str = "+"+offset_str
            str_value += offset_str
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
    offset: timedelta | None

    def __str__(self) -> str:
        str_value = f"{self.element_id}.{self.event}"
        if self.offset is not None:
            offset_str = to_clock_value(self.offset)
            if not offset_str.startswith("-"):
                offset_str = "+"+offset_str
            str_value += offset_str
        return str_value


@dataclass
class RepeatValue:
    element_id: str
    repeat_number: int
    offset: timedelta | None

    def __str__(self) -> str:
        str_value = f"{self.element_id}.repeat({self.repeat_number})"
        if self.offset is not None:
            offset_str = to_clock_value(self.offset)
            if not offset_str.startswith("-"):
                offset_str = "+"+offset_str
            str_value += offset_str
        return str_value


@dataclass
class AccessKeyValue:
    key: str
    offset: timedelta | None

    def __str__(self) -> str:
        str_value = f'accessKey("{self.key}")'
        if self.offset is not None:
            offset_str = to_clock_value(self.offset)
            if not offset_str.startswith("-"):
                offset_str = "+"+offset_str
            str_value += offset_str
        return str_value


from datetime import datetime

class WallclockSyncValue:
    time: datetime

    def __str__(self) -> str:
        iso_time = self.time.isoformat(" ")
        return f"wallclock({iso_time})"

AnimationTimingEvent = Union[
    timedelta,
    SyncbaseValue,
    EventValue,
    RepeatValue,
    AccessKeyValue,
    WallclockSyncValue,
    Indefinite
]
 
def to_clock_value(delta: timedelta) -> str:
    seconds = delta.total_seconds()
    sign = ""
    if seconds < 0:
        sign = "-"
        seconds = abs(seconds)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    full_seconds = math.floor(seconds)
    partial_seconds = seconds - full_seconds
    if partial_seconds > 0:
        return f"{sign}{hours}:{minutes:02}:{full_seconds:02}{partial_seconds:.6f}"
    return f"{sign}{hours}:{minutes:02}:{full_seconds:02}"

