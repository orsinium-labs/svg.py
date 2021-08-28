from dataclasses import dataclass
from typing import Optional
from . import enums, values


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
    color_interpolation: Optional[enums.ColorInterpolation] = None


@dataclass
class FeFlood(AttrsMixin):
    flood_color: Optional[str] = None
    flood_opacity: Optional[values.Opacity] = None


@dataclass
class FilterPrimitives(AttrsMixin):
    color_interpolation_filters: Optional[enums.ColorInterpolation] = None


@dataclass
class FillStroke(AttrsMixin):
    fill: Optional[str] = None
    fill_opacity: Optional[values.Opacity] = None
    fill_rule: Optional[enums.ClipFillRule] = None
    stroke: Optional[str] = None
    stroke_dasharray: Optional[values.StrokeDashArray] = None
    stroke_dashoffset: Optional[values.StrokeDashOffset] = None
    stroke_linecap: Optional[enums.LineCap] = None
    stroke_linejoin: Optional[enums.LineJoin] = None
    stroke_miterlimit: Optional[values.StrokeMiterLimit] = None
    stroke_opacity: Optional[values.Opacity] = None
    stroke_width: Optional[values.StrokeWidth] = None


@dataclass
class FontSpecification(AttrsMixin):
    font_family: Optional[values.FontFamily] = None
    font_size: Optional[values.FontSize] = None
    font_size_adjust: Optional[values.FontSizeAdjust] = None
    font_stretch: Optional[enums.FontStretch] = None
    font_style = enums.FontStyle
    font_variant: Optional[enums.FontValiant] = None
    font_weight: Optional[enums.FontWeight] = None


@dataclass
class Gradients(AttrsMixin):
    stop_color: Optional[values.SVGColor] = None
    stop_opacity: Optional[values.Opacity] = None


@dataclass
class Graphics(AttrsMixin):
    clip_path: Optional[values.ClipPath] = None
    clip_rule: Optional[enums.ClipFillRule] = None
    cursor: Optional[enums.CursorValue] = None
    display: Optional[str] = None  # TODO
    filter: Optional[values.Filter] = None
    image_rendering: Optional[enums.Rendering] = None
    mask: Optional[values.Mask] = None
    opacity: Optional[values.Opacity] = None
    pointer_events: Optional[str] = None     # TODO
    shape_rendering: Optional[str] = None    # TODO
    text_rendering: Optional[str] = None     # TODO
    visibility: Optional[enums.Visibility] = None


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
    alignment_baseline: Optional[enums.TextAlignment] = None
    baseline_shift: Optional[enums.BaselineShift] = None
    direction: Optional[enums.TextDirection] = None
    dominant_baseline: Optional[enums.DominantBaseline] = None
    letter_spacing: Optional[enums.TextSpacing] = None
    text_anchor: Optional[enums.TextAnchor] = None
    text_decoration: Optional[enums.TextDecoration] = None
    unicode_bidi: Optional[str] = None  # TODO
    word_spacing: Optional[enums.TextSpacing] = None


@dataclass
class TextElements(AttrsMixin):
    writing_mode: Optional[str] = None  # TODO


@dataclass
class Viewports(AttrsMixin):
    overflow: Optional[enums.Overflow] = None


class Presentation(
    Color,
    FeFlood,
    FillStroke,
    FilterPrimitives,
    FontSpecification,
    Gradients,
    Graphics,
    Images,
    LightingEffects,
    Markers,
    TextContentElements,
    TextElements,
    Viewports,
):
    pass


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
    type: enums.ComponentTransferType
    tableValues: Optional[str] = None
    intercept: Optional[float] = None
    amplitude: Optional[float] = None
    exponent: Optional[float] = None
    offset: Optional[float] = None


@dataclass
class AnimValue(AttrsMixin):
    calcMode: Optional[enums.CalcMode] = None
    values: Optional[str] = None
    keyTimes: Optional[str] = None
    keySplines: Optional[str] = None
    by: Optional[str] = None
    from_: Optional[str] = None
    to: Optional[str] = None


# TODO: anim*Attrs
# TODO: descTitleMetadata
