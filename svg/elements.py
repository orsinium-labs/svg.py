from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Optional, Union

from typing_extensions import Literal

from . import _mixins as m, values
from ._transforms import Transform


@dataclass
class Element:
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/Core
    """

    element_name: ClassVar[str]

    elements: Optional[List['Element']] = None
    id: Optional[str] = None
    tabindex: Optional[int] = None
    lang: Optional[str] = None
    xml__lang: Optional[str] = None

    transform_origin: Optional[str] = None
    style: Optional[values.StyleSheet] = None

    @classmethod
    def _as_str(cls, val: Any) -> str:
        if val is None:
            return ""
        if isinstance(val, Element):
            return str(val)
        if isinstance(val, Enum):
            return val.value
        if isinstance(val, bool):
            return str(val).lower()
        if isinstance(val, (list, tuple)):
            return ",".join(cls._as_str(v) for v in val)
        return str(val)

    def as_dict(self) -> Dict[str, str]:
        result = {}
        for key, val in asdict(self).items():
            if val is None:
                continue
            if key == "elements":
                continue
            key = key.rstrip("_")
            key = key.replace("__", ":")
            key = key.replace("_", "-")
            result[key] = self._as_str(val)
        return result

    def as_str(self) -> str:
        props = " ".join(f'{k}="{v}"' for k, v in self.as_dict().items())
        if self.elements:
            content = "".join(self._as_str(e) for e in self.elements)
            return f"<{self.element_name} {props}>{content}</{self.element_name}>"
        return f"<{self.element_name} {props}/>"

    def __str__(self) -> str:
        return self.as_str()


@dataclass
class SVG(
    Element,
    m.GraphicsElementEvents,
    m.Color,
    m.Graphics,
):
    element_name = "svg"
    viewBox: Optional[values.ViewBoxSpec] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
    class_: Optional[values.Classes] = None
    mask: Optional[values.Mask] = None
    opacity: Optional[values.Opacity] = None
    clip_path: Optional[values.ClipPath] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None

    onunload: Optional[str] = None
    onabort: Optional[str] = None
    onerror: Optional[str] = None
    onresize: Optional[str] = None
    onscroll: Optional[str] = None
    onzoom: Optional[str] = None


@dataclass
class G(
    Element,
    m.GraphicsElementEvents,
    m.Color,
    m.Graphics,
):
    element_name = "g"
    transform: Optional[List[Transform]] = None
    class_: Optional[values.Classes] = None
    mask: Optional[values.Mask] = None
    opacity: Optional[values.Opacity] = None
    clip_path: Optional[values.ClipPath] = None


@dataclass
class Defs(
    Element,
    m.Color,
    m.GraphicsElementEvents,
):
    element_name = "defs"
    transform: Optional[List[Transform]] = None
    class_: Optional[values.Classes] = None
    pointer_events: Optional[str] = None  # TODO


@dataclass
class Desc(Element, m.GraphicsElementEvents):
    element_name = "desc"
    content: Optional[str] = None
    class_: Optional[values.Classes] = None


@dataclass
class Title(Element, m.GraphicsElementEvents):
    element_name = "title"
    content: Optional[str] = None
    class_: Optional[values.Classes] = None


@dataclass
class Symbol(
    Element,
    m.GraphicsElementEvents,
    m.Color,
    m.Graphics,
):
    element_name = "symbol"
    viewBox: Optional[values.ViewBoxSpec] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    refX: Union[values.Length, values.Number, None] = None
    refY: Union[values.Length, values.Number, None] = None
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    class_: Optional[values.Classes] = None
    mask: Optional[values.Mask] = None
    opacity: Optional[values.Opacity] = None
    clip_path: Optional[values.ClipPath] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class Image(
    Element,
    m.Color,
    m.Graphics,
    m.GraphicsElementEvents,
):
    element_name = "image"
    href: Optional[str] = None
    transform: Optional[List[Transform]] = None
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    image_rendering: Optional[Literal["auto", "optimizeSpeed", "optimizeQuality"]] = None
    class_: Optional[values.Classes] = None
    vector_effect: Optional[Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"]] = None
    visibility: Optional[Literal["visible", "hidden", "inherit"]] = None
    mask: Optional[values.Mask] = None
    opacity: Optional[values.Opacity] = None
    clip_path: Optional[values.ClipPath] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class Switch(Element, m.Color, m.GraphicsElementEvents):
    element_name = "switch"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    opacity: Optional[values.Opacity] = None
    class_: Optional[values.Classes] = None
    pointer_events: Optional[str] = None  # TODO


@dataclass
class Style(Element, m.GraphicsElementEvents):
    element_name = "style"
    type: Optional[values.ContentType] = None
    media: Optional[List[str]] = None
    title: Optional[str] = None


@dataclass
class _FigureElement(m.Color, m.GraphicsElementEvents, m.Graphics, m.FillStroke):
    pathLength: Optional[float] = None
    paint_order: Optional[Literal["normal", "fill", "stroke", "markers"]] = None
    shape_rendering: Optional[Literal["auto", "optimizeSpeed", "crispEdges", "geometricPrecision", "inherit"]] = None
    class_: Optional[values.Classes] = None
    vector_effect: Optional[Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"]] = None
    visibility: Optional[Literal["visible", "hidden", "inherit"]] = None
    mask: Optional[values.Mask] = None
    opacity: Optional[values.Opacity] = None
    clip_path: Optional[values.ClipPath] = None


@dataclass
class Path(Element, _FigureElement):
    element_name = "path"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    d: Optional[List[values.PathData]] = None
    marker_start: Optional[values.Marker] = None
    marker_mid: Optional[values.Marker] = None
    marker_end: Optional[values.Marker] = None
    stroke_linecap: Optional[Literal["butt", "round", "square", "inherit"]] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[values.Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    fill_opacity: Optional[values.Opacity] = None
    fill: Optional[str] = None


@dataclass
class Rect(Element, _FigureElement):
    element_name = "rect"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
    rx: Union[values.Length, values.Number, None] = None
    ry: Union[values.Length, values.Number, None] = None
    marker_start: Optional[values.Marker] = None
    marker_mid: Optional[values.Marker] = None
    marker_end: Optional[values.Marker] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[values.Number] = None
    fill_opacity: Optional[values.Opacity] = None
    fill: Optional[str] = None


@dataclass
class Circle(Element, _FigureElement):
    element_name = "circle"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    cx: Union[values.Length, values.Number, None] = None
    cy: Union[values.Length, values.Number, None] = None
    r: Union[values.Length, values.Number, None] = None
    marker_mid: Optional[values.Marker] = None
    fill_opacity: Optional[values.Opacity] = None
    fill: Optional[str] = None


@dataclass
class Ellipse(Element, _FigureElement):
    element_name = "ellipse"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    cx: Union[values.Length, values.Number, None] = None
    cy: Union[values.Length, values.Number, None] = None
    rx: Union[values.Length, values.Number, None] = None
    ry: Union[values.Length, values.Number, None] = None
    marker_start: Optional[values.Marker] = None
    marker_mid: Optional[values.Marker] = None
    marker_end: Optional[values.Marker] = None
    fill_opacity: Optional[values.Opacity] = None
    fill: Optional[str] = None


@dataclass
class Line(Element, _FigureElement):
    element_name = "line"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    x1: Union[values.Length, values.Number, None] = None
    y1: Union[values.Length, values.Number, None] = None
    x2: Union[values.Length, values.Number, None] = None
    y2: Union[values.Length, values.Number, None] = None
    marker_start: Optional[values.Marker] = None
    marker_mid: Optional[values.Marker] = None
    marker_end: Optional[values.Marker] = None
    stroke_linecap: Optional[Literal["butt", "round", "square", "inherit"]] = None


@dataclass
class Polyline(Element, _FigureElement):
    element_name = "polyline"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    points: Optional[List[values.Number]] = None
    marker_start: Optional[values.Marker] = None
    marker_mid: Optional[values.Marker] = None
    marker_end: Optional[values.Marker] = None
    stroke_linecap: Optional[Literal["butt", "round", "square", "inherit"]] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[values.Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    fill_opacity: Optional[values.Opacity] = None
    fill: Optional[str] = None


@dataclass
class Polygon(Element, _FigureElement):
    element_name = "polygon"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    points: Optional[List[values.Number]] = None
    marker_start: Optional[values.Marker] = None
    marker_mid: Optional[values.Marker] = None
    marker_end: Optional[values.Marker] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[values.Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    fill_opacity: Optional[values.Opacity] = None
    fill: Optional[str] = None


@dataclass
class _TextElement(
    m.FontSpecification,
    m.TextContentElements,
    m.Color,
    m.GraphicsElementEvents,
    m.Graphics,
    m.FillStroke,
):
    paint_order: Optional[Literal["normal", "fill", "stroke", "markers"]] = None
    class_: Optional[values.Classes] = None
    vector_effect: Optional[Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"]] = None
    visibility: Optional[Literal["visible", "hidden", "inherit"]] = None
    fill_opacity: Optional[values.Opacity] = None
    fill: Optional[str] = None


@dataclass
class Text(Element, _TextElement):
    element_name = "text"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    dx: Union[values.Length, values.Number, None] = None
    dy: Union[values.Length, values.Number, None] = None
    textLength: Union[values.Length, values.Number, None] = None
    lengthAdjust: Optional[Literal["spacing", "spacingAndGlyphs"]] = None
    writing_mode: Optional[Literal["horizontal-tb", "vertical-rl", "vertical-lr"]] = None
    text_rendering: Optional[Literal["auto", "optimizeSpeed", "optimizeLegibility", "geometricPrecision"]] = None
    stroke_linecap: Optional[Literal["butt", "round", "square", "inherit"]] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[values.Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    mask: Optional[values.Mask] = None
    opacity: Optional[values.Opacity] = None
    clip_path: Optional[values.ClipPath] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class TSpan(Element, _TextElement):
    element_name = "tspan"
    externalResourcesRequired: Optional[bool] = None
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    dx: Union[values.Length, values.Number, None] = None
    dy: Union[values.Length, values.Number, None] = None
    textLength: Union[values.Length, values.Number, None] = None
    lengthAdjust: Optional[Literal["spacing", "spacingAndGlyphs"]] = None
    writing_mode: Optional[Literal["horizontal-tb", "vertical-rl", "vertical-lr"]] = None
    alignment_baseline: Optional[Literal[
        "baseline", "top", "before-edge", "text-top",
        "text-before-edge", "middle", "bottom",
        "after-edge", "text-bottom", "text-after-edge", "ideographic",
        "lower", "hanging", "mathematical", "inherit",
    ]] = None
    baseline_shift: Optional[Literal["baseline", "sub", "super", "inherit"]] = None
    stroke_linecap: Optional[Literal["butt", "round", "square", "inherit"]] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[values.Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    opacity: Optional[values.Opacity] = None


@dataclass
class TextPath(Element, _TextElement):
    element_name = "textPath"
    externalResourcesRequired: Optional[bool] = None
    startOffset: Optional[str] = None
    textLength: Union[values.Length, values.Number, None] = None
    lengthAdjust: Optional[Literal["spacing", "spacingAndGlyphs"]] = None
    method: Optional[Literal["align", "stretch"]] = None
    spacing: Optional[Literal["auto", "exact"]] = None
    href: Optional[str] = None
    path: Optional[str] = None
    side: Optional[Literal["left", "right"]] = None
    writing_mode: Optional[Literal["horizontal-tb", "vertical-rl", "vertical-lr"]] = None
    alignment_baseline: Optional[Literal[
        "baseline", "top", "before-edge", "text-top",
        "text-before-edge", "middle", "bottom",
        "after-edge", "text-bottom", "text-after-edge", "ideographic",
        "lower", "hanging", "mathematical", "inherit",
    ]] = None
    baseline_shift: Optional[Literal["baseline", "sub", "super", "inherit"]] = None
    stroke_linecap: Optional[Literal["butt", "round", "square", "inherit"]] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[values.Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    opacity: Optional[values.Opacity] = None


@dataclass
class Marker(Element, m.Color, m.GraphicsElementEvents, m.Graphics):
    element_name = "marker"
    externalResourcesRequired: Optional[bool] = None
    viewBox: Optional[values.ViewBoxSpec] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    refX: Union[values.Length, values.Number, None] = None
    refY: Union[values.Length, values.Number, None] = None
    markerUnits: Optional[Literal["strokeWidth", "userSpaceOnUse", "userSpace"]] = None
    markerWidth: Union[values.Length, values.Number, None] = None
    markerHeight: Union[values.Length, values.Number, None] = None
    orient: Optional[str] = None
    opacity: Optional[values.Opacity] = None
    clip_path: Optional[values.ClipPath] = None
    class_: Optional[values.Classes] = None
    mask: Optional[values.Mask] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class ColorProfile(Element):
    element_name = "color-profile"
    local: Optional[str] = None


@dataclass
class _Gradient:
    externalResourcesRequired: Optional[bool] = None
    gradientUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    gradientTransform: Optional[List[Transform]] = None
    spreadMethod: Optional[Literal["pad", "reflect", "repeat"]] = None
    href: Optional[str] = None
    class_: Optional[values.Classes] = None


@dataclass
class LinearGradient(Element, _Gradient, m.Color, m.GraphicsElementEvents):
    element_name = "linearGradient"
    x1: Union[values.Length, values.Number, None] = None
    y1: Union[values.Length, values.Number, None] = None
    x2: Union[values.Length, values.Number, None] = None
    y2: Union[values.Length, values.Number, None] = None


@dataclass
class RadialGradient(Element, _Gradient, m.Color, m.GraphicsElementEvents):
    element_name = "radialGradient"
    cx: Union[values.Length, values.Number, None] = None
    cy: Union[values.Length, values.Number, None] = None
    r: Union[values.Length, values.Number, None] = None
    fr: Union[values.Length, values.Number, None] = None
    fx: Union[values.Length, values.Number, None] = None
    fy: Union[values.Length, values.Number, None] = None


@dataclass
class Stop(Element, m.GraphicsElementEvents):
    element_name = "stop"
    offset: Union[values.Length, values.Number, None] = None
    stop_opacity: Optional[values.Opacity] = None
    stop_color: Optional[str] = None
    class_: Optional[values.Classes] = None


@dataclass
class Pattern(Element, m.Color, m.GraphicsElementEvents, m.Graphics):
    element_name = "pattern"
    externalResourcesRequired: Optional[bool] = None
    viewBox: Optional[values.ViewBoxSpec] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    patternUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    patternTransform: Optional[List[Transform]] = None
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
    patternContentUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    href: Optional[str] = None
    class_: Optional[values.Classes] = None
    mask: Optional[values.Mask] = None
    clip_path: Optional[values.ClipPath] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class ClipPath(Element, m.Color, m.Graphics):
    element_name = "clipPath"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    clipPathUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    class_: Optional[values.Classes] = None
    mask: Optional[values.Mask] = None
    clip_path: Optional[values.ClipPath] = None


@dataclass
class Mask(Element, m.Color, m.Graphics):
    element_name = "mask"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    maskUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
    maskContentUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    class_: Optional[values.Classes] = None
    mask: Optional[values.Mask] = None
    clip_path: Optional[values.ClipPath] = None


@dataclass
class A(Element, m.Color, m.GraphicsElementEvents, m.Graphics):
    element_name = "a"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    target: Optional[Literal["_self", "_parent", "_top", "_blank"]] = None
    href: Optional[str] = None
    class_: Optional[values.Classes] = None
    visibility: Optional[Literal["visible", "hidden", "inherit"]] = None
    mask: Optional[values.Mask] = None
    opacity: Optional[values.Opacity] = None
    clip_path: Optional[values.ClipPath] = None


@dataclass
class View(Element, m.GraphicsElementEvents):
    element_name = "view"
    externalResourcesRequired: Optional[bool] = None
    viewBox: Optional[values.ViewBoxSpec] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None


@dataclass
class Script(Element, m.GraphicsElementEvents):
    element_name = "script"
    externalResourcesRequired: Optional[bool] = None
    type: Optional[str] = None
    href: Optional[str] = None


@dataclass
class Animate(Element, m.Animation, m.Color, m.AnimationTiming, m.GraphicsElementEvents):
    element_name = "animate"
    externalResourcesRequired: Optional[bool] = None
    keyPoints: Optional[str] = None
    attributeName: Optional[str] = None


@dataclass
class Set(Element, m.AnimationTiming, m.GraphicsElementEvents):
    element_name = "set"
    externalResourcesRequired: Optional[bool] = None
    to: Optional[str] = None
    min: Optional[str] = None
    keyPoints: Optional[str] = None
    attributeName: Optional[str] = None
    href: Optional[str] = None


@dataclass
class AnimateMotion(Element, m.Animation, m.AnimationTiming, m.GraphicsElementEvents):
    element_name = "animateMotion"
    externalResourcesRequired: Optional[bool] = None
    path: Optional[str] = None
    keyPoints: Optional[str] = None
    rotate: Optional[str] = None
    origin: Optional[str] = None


@dataclass
class MPath(Element, m.GraphicsElementEvents):
    element_name = "mpath"
    externalResourcesRequired: Optional[bool] = None
    href: Optional[str] = None


@dataclass
class AnimateTransform(Element, m.Animation, m.AnimationTiming, m.GraphicsElementEvents):
    element_name = "animateTransform"
    externalResourcesRequired: Optional[bool] = None
    type: Optional[Literal["translate", "scale", "rotate", "skewX", "skewY"]] = None
    keyPoints: Optional[str] = None
    attributeName: Optional[str] = None


@dataclass
class DefinitionSrc(Element):
    element_name = "definition-src"
    pass


@dataclass
class Metadata(Element, m.GraphicsElementEvents):
    element_name = "metadata"
    pass


@dataclass
class ForeignObject(Element, m.Color, m.GraphicsElementEvents, m.Graphics):
    element_name = "foreignObject"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[List[Transform]] = None
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
    content: Optional[str] = None
    class_: Optional[values.Classes] = None
    vector_effect: Optional[Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"]] = None
    visibility: Optional[Literal["visible", "hidden", "inherit"]] = None
    opacity: Optional[values.Opacity] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class Use(Element, m.GraphicsElementEvents, m.Color, m.Graphics):
    element_name = "use"
    href: Optional[str] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[List[Transform]] = None
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
    vector_effect: Optional[Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"]] = None
    opacity: Optional[values.Opacity] = None
    clip_path: Optional[values.ClipPath] = None
    mask: Optional[values.Mask] = None
