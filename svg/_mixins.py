from dataclasses import dataclass
from typing import Optional
from . import values
from typing_extensions import Literal


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
class DocumentEvents(AttrsMixin):
    onunload: Optional[str] = None
    onabort: Optional[str] = None
    onerror: Optional[str] = None
    onresize: Optional[str] = None
    onscroll: Optional[str] = None
    onzoom: Optional[str] = None


@dataclass
class Color(AttrsMixin):
    color: Optional[str] = None
    color_interpolation: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None


@dataclass
class FeFlood(AttrsMixin):
    flood_color: Optional[str] = None
    flood_opacity: Optional[values.Opacity] = None


@dataclass
class FilterPrimitives(AttrsMixin):
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None


@dataclass
class FillStroke(AttrsMixin):
    fill: Optional[str] = None
    fill_opacity: Optional[values.Opacity] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    stroke: Optional[str] = None
    stroke_dasharray: Optional[values.StrokeDashArray] = None
    stroke_dashoffset: Optional[values.StrokeDashOffset] = None
    stroke_linecap: Optional[Literal["butt", "round", "square", "inherit"]] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[values.StrokeMiterLimit] = None
    stroke_opacity: Optional[values.Opacity] = None
    stroke_width: Optional[values.StrokeWidth] = None


@dataclass
class FontSpecification(AttrsMixin):
    font_family: Optional[values.FontFamily] = None
    font_size: Optional[values.FontSize] = None
    font_size_adjust: Optional[values.FontSizeAdjust] = None
    font_stretch: Optional[
        Literal[
            "normal",
            "wider",
            "narrower",
            "ultra-condensed",
            "extra-condensed",
            "semi-condensed",
            "semi-expanded",
            "expanded",
            "extra-expanded",
            "ultra-expanded",
            "inherit",
        ]
    ] = None
    font_style: Optional[Literal["normal", "italic", "oblique", "inherit"]] = None
    font_variant: Optional[Literal["normal", "small-caps", "inherit"]] = None
    font_weight: Optional[
        Literal[
            "normal",
            "bold",
            "bolder",
            "lighter",
            "inherit",
            "100",
            "200",
            "300",
            "400",
            "500",
            "600",
            "700",
            "800",
            "900",
        ]
    ] = None


@dataclass
class Gradients(AttrsMixin):
    stop_color: Optional[values.SVGColor] = None
    stop_opacity: Optional[values.Opacity] = None


@dataclass
class Graphics(AttrsMixin):
    clip_path: Optional[values.ClipPath] = None
    clip_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    cursor: Optional[
        Literal[
            "auto",
            "crosshair",
            "default",
            "pointer",
            "move",
            "e-resize",
            "ne-resize",
            "nw-resize",
            "n-resize",
            "se-resize",
            "sw-resize",
            "s-resize",
            "w-resize",
            "text",
            "wait",
            "help",
            "inherit",
        ]
    ] = None
    display: Optional[str] = None  # TODO
    filter: Optional[values.Filter] = None
    image_rendering: Optional[
        Literal["auto", "optimizeSpeed", "optimizeQuality", "inherit"]
    ] = None
    mask: Optional[values.Mask] = None
    opacity: Optional[values.Opacity] = None
    pointer_events: Optional[str] = None  # TODO
    shape_rendering: Optional[str] = None  # TODO
    text_rendering: Optional[str] = None  # TODO
    visibility: Optional[Literal["visible", "hidden", "inherit"]] = None
    vector_effect: Optional[
        Literal[
            "none",
            "non-scaling-stroke",
            "non-scaling-size",
            "non-rotation",
            "fixed-position",
        ]
    ] = None
    paint_order: Optional[Literal["normal", "fill", "stroke", "markers"]] = None


class Images:
    pass  # TODO: no attrs, drop me


@dataclass
class LightingEffects(AttrsMixin):
    lighting_color: Optional[values.SVGColor] = None


@dataclass
class Markers(AttrsMixin):
    marker_start: Optional[values.Marker] = None
    marker_mid: Optional[values.Marker] = None
    marker_end: Optional[values.Marker] = None


@dataclass
class TextContentElements(AttrsMixin):
    alignment_baseline: Optional[
        Literal[
            "baseline",
            "top",
            "before-edge",
            "text-top",
            "text-before-edge",
            "middle",
            "bottom",
            "after-edge",
            "text-bottom",
            "text-after-edge",
            "ideographic",
            "lower",
            "hanging",
            "mathematical",
            "inherit",
        ]
    ] = None
    baseline_shift: Optional[Literal["baseline", "sub", "super", "inherit"]] = None
    direction: Optional[Literal["ltr", "rtl", "inherit"]] = None
    dominant_baseline: Optional[
        Literal[
            "auto",
            "autosense-script",
            "no-change",
            "reset",
            "ideographic",
            "lower",
            "hanging",
            "mathematical",
            "inherit",
        ]
    ] = None
    letter_spacing: Optional[Literal["auto", "exact"]] = None
    text_anchor: Optional[Literal["start", "middle", "end", "inherit"]] = None
    text_decoration: Optional[
        Literal["none", "underline", "overline", "line-through"]
    ] = None
    unicode_bidi: Optional[str] = None  # TODO
    word_spacing: Optional[Literal["auto", "exact"]] = None


@dataclass
class Viewports(AttrsMixin):
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class FilterPrimitive(AttrsMixin):
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    result: Optional[str] = None
    in_: Optional[str] = None


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

    # Animation attribute target attributes
    attributeName: Optional[str] = None


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
    fill: Optional[Literal["remove", "dtd"]] = None

# TODO: descTitleMetadata
