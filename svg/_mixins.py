from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta
from typing import TYPE_CHECKING, Any

from ._types import AnimationTimingEvent, Length, Number, TimeBezierPoint


if TYPE_CHECKING:
    from typing_extensions import Literal


class AttrsMixin:
    pass


@dataclass
class GraphicsElementEvents(AttrsMixin):
    onfocusin: str | None = None
    onfocusout: str | None = None
    onactivate: str | None = None
    onclick: str | None = None
    onmousedown: str | None = None
    onmouseup: str | None = None
    onmouseover: str | None = None
    onmousemove: str | None = None
    onmouseout: str | None = None
    onload: str | None = None


@dataclass
class Color(AttrsMixin):
    color: str | None = None
    color_interpolation: None | Literal[
        "auto", "sRGB", "linearRGB", "inherit",
    ] = None


@dataclass
class FillStroke(AttrsMixin):
    stroke: str | None = None
    stroke_dasharray: list[Number] | Literal["none"] | Length | None = None
    stroke_dashoffset: Literal["none"] | Length | Number | None = None
    stroke_opacity: Number | None = None
    stroke_width: Length | Number | None = None


@dataclass
class FontSpecification(AttrsMixin):
    font_family: str | None = None
    font_size: Length | Number | None = None
    font_size_adjust: Number | None | Literal["none"] = None
    font_style: None | Literal[
        "normal", "italic", "oblique", "inherit",
    ] = None
    font_variant: Literal["normal", "small-caps", "inherit"] | None = None
    font_weight: None | Literal[
        "normal", "bold", "bolder", "lighter", "inherit",
        "100", "200", "300", "400", "500", "600", "700", "800", "900",
    ] = None


@dataclass
class Graphics(AttrsMixin):
    clip_rule: Literal["evenodd", "nonzero", "inherit"] | None = None
    cursor: None | Literal[
        "auto", "crosshair", "default", "pointer", "move",
        "e-resize", "ne-resize", "nw-resize", "n-resize", "se-resize", "sw-resize", "s-resize", "w-resize",
        "text", "wait", "help", "inherit",
    ] = None
    display: str | None = None
    filter: str | None = None
    pointer_events: None | Literal[
        "bounding-box", "visiblePainted", "visibleFill", "visibleStroke",
        "visible", "painted", "fill", "stroke", "all", "none",
    ] = None


@dataclass
class TextContentElements(AttrsMixin):
    direction: Literal["ltr", "rtl", "inherit"] | None = None
    dominant_baseline: None | Literal[
        "auto", "autosense-script", "no-change", "reset", "ideographic",
        "lower", "hanging", "mathematical", "inherit",
        "text-bottom", "alphabetic", "middle", "central", "text-top",
    ] = None
    letter_spacing: Literal["auto", "exact"] | None = None
    text_anchor: Literal["start", "middle", "end", "inherit"] | None = None
    text_decoration: None | Literal[
        "none", "underline", "overline", "line-through",
    ] = None
    unicode_bidi: None | Literal[
        "normal", "embed", "isolate", "bidi-override", "isolate-override", "plaintext",
    ] = None
    word_spacing: Literal["auto", "exact"] | None = None


@dataclass
class FilterPrimitive(AttrsMixin):
    x: Length | Number | None = None
    y: Length | Number | None = None


@dataclass
class ComponentTransferFunction(AttrsMixin):
    type: Literal["identity", "table", "discrete", "linear", "gamma"]
    tableValues: str | None = None
    intercept: float | None = None
    amplitude: float | None = None
    exponent: float | None = None
    offset: float | None = None


@dataclass
class Animation(AttrsMixin):
    # Animation value attributes
    calcMode: Literal["discrete", "linear", "paced", "spline"] | None = None
    values: str | list[Any] | None = None
    keyTimes: list[Number] | None = None
    keySplines: list[TimeBezierPoint] | None = None
    keyPoints: list[Number] | None = None
    from_: str | None = None
    to: str | None = None
    by: str | None = None

    # Animation target element attributes
    href: str | None = None

    # Animation addition attributes
    additive: Literal["replace", "sum"] | None = None
    accumulate: Literal["none", "sum"] | None = None


@dataclass
class AnimationTiming(AttrsMixin):
    begin: AnimationTimingEvent | list[AnimationTimingEvent] | None = None
    dur: timedelta | Literal["media", "indefinite"] | None = None
    end: AnimationTimingEvent | list[AnimationTimingEvent] | None = None
    min: timedelta | None = None
    max: timedelta | None = None
    restart: Literal["always", "never", "whenNotActive"] | None = None
    repeatCount: Number | Literal["indefinite"] | None = None
    repeatDur: timedelta | Literal["indefinite"] | None = None
    fill: Literal["freeze", "remove"] | None = None
