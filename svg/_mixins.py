from dataclasses import dataclass
from typing import Optional
from . import enums, values


class AttrsMixin:
    pass


@dataclass
class STDAttrs(AttrsMixin):
    id: Optional[str] = None


@dataclass
class GraphicsElementEvents(AttrsMixin):
    onfocusin: str
    onfocusout: str
    onactivate: str
    onclick: str
    onmousedown: str
    onmouseup: str
    onmouseover: str
    onmousemove: str
    onmouseout: str
    onload: str


@dataclass
class DocumentEvents(AttrsMixin):
    onunload: str
    onabort: str
    onerror: str
    onresize: str
    onscroll: str
    onzoom: str


@dataclass
class Color(AttrsMixin):
    color: str
    color_interpolation: enums.ColorInterpolation
    color_rendering: enums.Rendering


@dataclass
class Containers(AttrsMixin):
    enable_background: values.EnableBackground


@dataclass
class FeFlood(AttrsMixin):
    flood_color: str
    flood_opacity: values.Opacity


@dataclass
class FilterPrimitives(AttrsMixin):
    color_interpolation_filters: enums.ColorInterpolation


@dataclass
class FillStroke(AttrsMixin):
    fill: str
    fill_opacity: values.Opacity
    fill_rule: enums.ClipFillRule
    stroke: str
    stroke_dasharray: values.StrokeDashArray
    stroke_dashoffset: values.StrokeDashOffset
    stroke_linecap: enums.LineCap
    stroke_linejoin: enums.LineJoin
    stroke_miterlimit: values.StrokeMiterLimit
    stroke_opacity: values.Opacity
    stroke_width: values.StrokeWidth


@dataclass
class FontSpecification(AttrsMixin):
    font_family: values.FontFamily
    font_size: values.FontSize
    font_size_adjust: values.FontSizeAdjust
    font_stretch: enums.FontStretch
    font_style = enums.FontStyle
    font_variant: enums.FontValiant
    font_weight: enums.FontWeight


@dataclass
class Gradients(AttrsMixin):
    stop_color: values.SVGColor
    stop_opacity: values.Opacity


@dataclass
class Graphics(AttrsMixin):
    clip_path: values.ClipPath
    clip_rule: enums.ClipFillRule
    cursor: enums.CursorValue
    display: str  # TODO
    filter: values.Filter
    image_rendering: enums.Rendering
    mask: values.Mask
    opacity: values.Opacity
    pointer_events: str     # TODO
    shape_rendering: str    # TODO
    text_rendering: str     # TODO
    visibility: enums.Visibility


class Images:
    pass  # TODO: no attrs, drop me


@dataclass
class LightingEffects(AttrsMixin):
    lighting_color: values.SVGColor


@dataclass
class Markers(AttrsMixin):
    marker_start: values.Marker
    marker_mid: values.Marker
    marker_end: values.Marker


@dataclass
class TextContentElements(AttrsMixin):
    alignment_baseline: enums.TextAlignment
    baseline_shift: enums.BaselineShift
    direction: enums.TextDirection
    dominant_baseline: enums.DominantBaseline
    glyph_orientation_horizontal: values.GlyphOrientationHorizontal
    glyph_orientation_vertical: values.GlyphOrientationVertical
    letter_spacing: values.Spacing
    text_anchor: enums.TextAnchor
    text_decoration: enums.TextDecoration
    unicode_bidi: str  # TODO
    word_spacing: values.Spacing


@dataclass
class TextElements(AttrsMixin):
    writing_mode: str  # TODO


@dataclass
class Viewports(AttrsMixin):
    clip: values.Clip
    overflow: enums.Overflow


class Presentation(
    Color,
    Containers,
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
    x: values.Coordinate
    y: values.Coordinate
    width: values.Length
    height: values.Length
    result: str
    in_: str
