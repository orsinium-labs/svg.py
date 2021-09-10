from dataclasses import dataclass
from typing import List, Optional, Union

from typing_extensions import Literal

from ._types import Length, Number


class AttrsMixin:
    pass


@dataclass
class GraphicsElementEvents(AttrsMixin):
    onfocusin: Optional[str] = None
    onfocusout: Optional[str] = None
    onactivate: Optional[str] = None
    onclick: Optional[str] = None
    onmousedown: Optional[str] = None
    onmouseup: Optional[str] = None
    onmouseover: Optional[str] = None
    onmousemove: Optional[str] = None
    onmouseout: Optional[str] = None
    onload: Optional[str] = None


@dataclass
class Color(AttrsMixin):
    color: Optional[str] = None
    color_interpolation: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None


@dataclass
class FillStroke(AttrsMixin):
    stroke: Optional[str] = None
    stroke_dasharray: Union[List[Number], Literal["none"], Length, None] = None
    stroke_dashoffset: Union[Literal["none"], Length, Number, None] = None
    stroke_opacity: Optional[Number] = None
    stroke_width: Union[Length, Number, None] = None


@dataclass
class FontSpecification(AttrsMixin):
    font_family: Optional[str] = None
    font_size: Union[Length, Number, None] = None
    font_size_adjust: Union[Number, None, Literal["none"]] = None
    font_stretch: Optional[Literal[
        "normal", "wider", "narrower",
        "ultra-condensed", "extra-condensed", "semi-condensed",
        "semi-expanded", "expanded", "extra-expanded", "ultra-expanded",
        "inherit",
    ]] = None
    font_style: Optional[Literal["normal", "italic", "oblique", "inherit"]] = None
    font_variant: Optional[Literal["normal", "small-caps", "inherit"]] = None
    font_weight: Optional[Literal[
        "normal", "bold", "bolder", "lighter", "inherit",
        "100", "200", "300", "400", "500", "600", "700", "800", "900",
    ]] = None


@dataclass
class Graphics(AttrsMixin):
    clip_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    cursor: Optional[Literal[
        "auto", "crosshair", "default", "pointer", "move",
        "e-resize", "ne-resize", "nw-resize", "n-resize", "se-resize", "sw-resize", "s-resize", "w-resize",
        "text", "wait", "help", "inherit",
    ]] = None
    display: Optional[str] = None
    filter: Optional[str] = None
    pointer_events: Optional[Literal[
        "bounding-box", "visiblePainted", "visibleFill", "visibleStroke",
        "visible", "painted", "fill", "stroke", "all", "none",
    ]] = None


@dataclass
class TextContentElements(AttrsMixin):
    direction: Optional[Literal["ltr", "rtl", "inherit"]] = None
    dominant_baseline: Optional[Literal[
        "auto", "autosense-script", "no-change", "reset", "ideographic",
        "lower", "hanging", "mathematical", "inherit",
    ]] = None
    letter_spacing: Optional[Literal["auto", "exact"]] = None
    text_anchor: Optional[Literal["start", "middle", "end", "inherit"]] = None
    text_decoration: Optional[Literal["none", "underline", "overline", "line-through"]] = None
    unicode_bidi: Optional[Literal["normal", "embed", "isolate", "bidi-override", "isolate-override", "plaintext"]] = None
    word_spacing: Optional[Literal["auto", "exact"]] = None


@dataclass
class FilterPrimitive(AttrsMixin):
    x: Union[Length, Number, None] = None
    y: Union[Length, Number, None] = None


@dataclass
class ComponentTransferFunction(AttrsMixin):
    type: Literal["identity", "table", "discrete", "linear", "gamma"]
    tableValues: Optional[str] = None
    intercept: Optional[float] = None
    amplitude: Optional[float] = None
    exponent: Optional[float] = None
    offset: Optional[float] = None


@dataclass
class Animation(AttrsMixin):
    # Animation value attributes
    calcMode: Optional[Literal["discrete", "linear", "paced", "spline"]] = None
    values: Optional[str] = None
    keyTimes: Optional[str] = None
    keySplines: Optional[str] = None
    from_: Optional[str] = None
    to: Optional[str] = None
    by: Optional[str] = None

    # Animation target element attributes
    href: Optional[str] = None

    # Animation addition attributes
    additive: Optional[Literal["replace", "sum"]] = None
    accumulate: Optional[Literal["none", "sum"]] = None


@dataclass
class AnimationTiming(AttrsMixin):
    begin: Optional[str] = None
    dur: Optional[str] = None
    end: Optional[str] = None
    min: Optional[str] = None
    max: Optional[str] = None
    restart: Optional[Literal["always", "never", "whenNotActive"]] = None
    repeatCount: Optional[str] = None
    repeatDur: Optional[str] = None
