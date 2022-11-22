from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Optional

from . import _mixins as m
from ._path import PathData
from ._transforms import Transform
from ._types import Length, Number, PreserveAspectRatio, ViewBoxSpec

if TYPE_CHECKING:
    from typing_extensions import Literal


@dataclass
class Element:
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/Core
    """

    element_name: ClassVar[str]

    elements: Optional[list['Element']] = None
    text: Optional[str] = None
    id: Optional[str] = None
    tabindex: Optional[int] = None
    lang: Optional[str] = None

    transform_origin: Optional[str] = None
    style: Optional[str] = None

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
            return " ".join(cls._as_str(v) for v in val)
        return str(val)

    def as_dict(self) -> dict[str, str]:
        result = {}
        for key, val in vars(self).items():
            if val is None:
                continue
            if key in ("elements", "text"):
                continue
            key = key.rstrip("_")
            key = key.replace("__", ":")
            key = key.replace("_", "-")
            result[key] = self._as_str(val)
        return result

    def as_str(self) -> str:
        props = " ".join(f'{k}="{v}"' for k, v in self.as_dict().items())
        if self.text:
            return f"<{self.element_name} {props}>{self.text}</{self.element_name}>"
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
    """The svg element is a container that defines a new coordinate system and viewport.

    It is used as the outermost element of SVG documents, but it can also be used
    to embed an SVG fragment inside an SVG or HTML document.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg
    """
    element_name = "svg"
    xmlns: Optional[str] = "http://www.w3.org/2000/svg"
    viewBox: Optional[ViewBoxSpec] = None
    preserveAspectRatio: Optional[PreserveAspectRatio] = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    class_: Optional[list[str]] = None
    mask: Optional[str] = None
    opacity: Optional[Number] = None
    clip_path: Optional[str] = None
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
    """The <g> SVG element is a container used to group other SVG elements.

    Transformations applied to the <g> element are performed on its child elements,
    and its attributes are inherited by its children. It can also group multiple elements
    to be referenced later with the <use> element.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/g
    """
    element_name = "g"
    transform: Optional[list[Transform]] = None
    class_: Optional[list[str]] = None
    mask: Optional[str] = None
    opacity: Optional[Number] = None
    clip_path: Optional[str] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    fill_opacity: Optional[Number] = None
    fill: Optional[str] = None


@dataclass
class Defs(
    Element,
    m.Color,
    m.GraphicsElementEvents,
):
    """The <defs> is used to store graphical objects that will be used at a later time.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/defs
    """
    element_name = "defs"
    transform: Optional[list[Transform]] = None
    class_: Optional[list[str]] = None
    pointer_events: Optional[str] = None  # TODO


@dataclass
class Desc(Element, m.GraphicsElementEvents):
    """The <desc> element provides an accessible, long-text description of any element.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/desc
    """
    element_name = "desc"
    content: Optional[str] = None
    class_: Optional[list[str]] = None


@dataclass
class Title(Element, m.GraphicsElementEvents):
    """The <title> element provides an accessible, short-text description of any element.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/title
    """
    element_name = "title"
    content: Optional[str] = None
    class_: Optional[list[str]] = None


@dataclass
class Symbol(
    Element,
    m.GraphicsElementEvents,
    m.Color,
    m.Graphics,
):
    """The <symbol> is used to define template objects which can be used by a <use> element.

    The use of <symbol> elements for graphics that are used multiple times in the same
    document adds structure and semantics. Documents that are rich in structure may be
    rendered graphically, as speech, or as Braille, and thus promote accessibility.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/symbol
    """
    element_name = "symbol"
    viewBox: Optional[ViewBoxSpec] = None
    preserveAspectRatio: Optional[PreserveAspectRatio] = None
    refX: Length | Number | None = None
    refY: Length | Number | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    class_: Optional[list[str]] = None
    mask: Optional[str] = None
    opacity: Optional[Number] = None
    clip_path: Optional[str] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class Image(
    Element,
    m.Color,
    m.Graphics,
    m.GraphicsElementEvents,
):
    """The <image> SVG element includes images inside SVG documents.

    The only image formats SVG software must support are JPEG, PNG, and other SVG files.
    Animated GIF behavior is undefined.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/image
    """
    element_name = "image"
    href: Optional[str] = None
    transform: Optional[list[Transform]] = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    preserveAspectRatio: Optional[PreserveAspectRatio] = None
    image_rendering: Optional[Literal["auto", "optimizeSpeed", "optimizeQuality"]] = None
    class_: Optional[list[str]] = None
    vector_effect: Optional[Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"]] = None
    visibility: Optional[Literal["visible", "hidden", "inherit"]] = None
    mask: Optional[str] = None
    opacity: Optional[Number] = None
    clip_path: Optional[str] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class Switch(Element, m.Color, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/switch
    """
    element_name = "switch"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    opacity: Optional[Number] = None
    class_: Optional[list[str]] = None
    pointer_events: Optional[str] = None  # TODO


@dataclass
class Style(Element, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/style
    """
    element_name = "style"
    type: Optional[str] = None
    media: Optional[list[str]] = None
    title: Optional[str] = None


@dataclass
class _FigureElement(m.Color, m.GraphicsElementEvents, m.Graphics, m.FillStroke):
    pathLength: Optional[float] = None
    paint_order: Optional[Literal["normal", "fill", "stroke", "markers"]] = None
    shape_rendering: Optional[Literal["auto", "optimizeSpeed", "crispEdges", "geometricPrecision", "inherit"]] = None
    class_: Optional[list[str]] = None
    vector_effect: Optional[Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"]] = None
    visibility: Optional[Literal["visible", "hidden", "inherit"]] = None
    mask: Optional[str] = None
    opacity: Optional[Number] = None
    clip_path: Optional[str] = None


@dataclass
class Path(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/path
    """
    element_name = "path"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    d: Optional[list[PathData]] = None
    marker_start: Optional[str] = None
    marker_mid: Optional[str] = None
    marker_end: Optional[str] = None
    stroke_linecap: Optional[Literal["butt", "round", "square", "inherit"]] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    fill_opacity: Optional[Number] = None
    fill: Optional[str] = None


@dataclass
class Rect(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/rect
    """
    element_name = "rect"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    rx: Length | Number | None = None
    ry: Length | Number | None = None
    marker_start: Optional[str] = None
    marker_mid: Optional[str] = None
    marker_end: Optional[str] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[Number] = None
    fill_opacity: Optional[Number] = None
    fill: Optional[str] = None


@dataclass
class Circle(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/circle
    """
    element_name = "circle"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    cx: Length | Number | None = None
    cy: Length | Number | None = None
    r: Length | Number | None = None
    marker_mid: Optional[str] = None
    fill_opacity: Optional[Number] = None
    fill: Optional[str] = None


@dataclass
class Ellipse(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/ellipse
    """
    element_name = "ellipse"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    cx: Length | Number | None = None
    cy: Length | Number | None = None
    rx: Length | Number | None = None
    ry: Length | Number | None = None
    marker_start: Optional[str] = None
    marker_mid: Optional[str] = None
    marker_end: Optional[str] = None
    fill_opacity: Optional[Number] = None
    fill: Optional[str] = None


@dataclass
class Line(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/line
    """
    element_name = "line"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    x1: Length | Number | None = None
    y1: Length | Number | None = None
    x2: Length | Number | None = None
    y2: Length | Number | None = None
    marker_start: Optional[str] = None
    marker_mid: Optional[str] = None
    marker_end: Optional[str] = None
    stroke_linecap: Optional[Literal["butt", "round", "square", "inherit"]] = None


@dataclass
class Polyline(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/polyline
    """
    element_name = "polyline"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    points: Optional[list[Number]] = None
    marker_start: Optional[str] = None
    marker_mid: Optional[str] = None
    marker_end: Optional[str] = None
    stroke_linecap: Optional[Literal["butt", "round", "square", "inherit"]] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    fill_opacity: Optional[Number] = None
    fill: Optional[str] = None


@dataclass
class Polygon(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/polygon
    """
    element_name = "polygon"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    points: Optional[list[Number]] = None
    marker_start: Optional[str] = None
    marker_mid: Optional[str] = None
    marker_end: Optional[str] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    fill_opacity: Optional[Number] = None
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
    class_: Optional[list[str]] = None
    vector_effect: Optional[Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"]] = None
    visibility: Optional[Literal["visible", "hidden", "inherit"]] = None
    fill_opacity: Optional[Number] = None
    fill: Optional[str] = None


@dataclass
class Text(Element, _TextElement):
    """The SVG <text> element draws a graphics element consisting of text.

    It's possible to apply a gradient, pattern, clipping path, mask, or filter to <text>,
    like any other SVG graphics element.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/text
    """
    element_name = "text"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    dx: Length | Number | None = None
    dy: Length | Number | None = None
    textLength: Length | Number | None = None
    lengthAdjust: Optional[Literal["spacing", "spacingAndGlyphs"]] = None
    writing_mode: Optional[Literal["horizontal-tb", "vertical-rl", "vertical-lr"]] = None
    text_rendering: Optional[Literal["auto", "optimizeSpeed", "optimizeLegibility", "geometricPrecision"]] = None
    stroke_linecap: Optional[Literal["butt", "round", "square", "inherit"]] = None
    stroke_linejoin: Optional[Literal["miter", "round", "bevel", "inherit"]] = None
    stroke_miterlimit: Optional[Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    mask: Optional[str] = None
    opacity: Optional[Number] = None
    clip_path: Optional[str] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class TSpan(Element, _TextElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/tspan
    """
    element_name = "tspan"
    externalResourcesRequired: Optional[bool] = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    dx: Length | Number | None = None
    dy: Length | Number | None = None
    textLength: Length | Number | None = None
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
    stroke_miterlimit: Optional[Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    opacity: Optional[Number] = None


@dataclass
class TextPath(Element, _TextElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/textPath
    """
    element_name = "textPath"
    externalResourcesRequired: Optional[bool] = None
    startOffset: Optional[str] = None
    textLength: Length | Number | None = None
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
    stroke_miterlimit: Optional[Number] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    opacity: Optional[Number] = None


@dataclass
class Marker(Element, m.Color, m.GraphicsElementEvents, m.Graphics):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/marker
    """
    element_name = "marker"
    externalResourcesRequired: Optional[bool] = None
    viewBox: Optional[ViewBoxSpec] = None
    preserveAspectRatio: Optional[PreserveAspectRatio] = None
    refX: Length | Number | None = None
    refY: Length | Number | None = None
    markerUnits: Optional[Literal["strokeWidth", "userSpaceOnUse", "userSpace"]] = None
    markerWidth: Length | Number | None = None
    markerHeight: Length | Number | None = None
    orient: Optional[str] = None
    opacity: Optional[Number] = None
    clip_path: Optional[str] = None
    class_: Optional[list[str]] = None
    mask: Optional[str] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class ColorProfile(Element):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/color
    """
    element_name = "color-profile"
    local: Optional[str] = None


@dataclass
class _Gradient:
    externalResourcesRequired: Optional[bool] = None
    gradientUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    gradientTransform: Optional[list[Transform]] = None
    spreadMethod: Optional[Literal["pad", "reflect", "repeat"]] = None
    href: Optional[str] = None
    class_: Optional[list[str]] = None


@dataclass
class LinearGradient(Element, _Gradient, m.Color, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/linearGradient
    """
    element_name = "linearGradient"
    x1: Length | Number | None = None
    y1: Length | Number | None = None
    x2: Length | Number | None = None
    y2: Length | Number | None = None


@dataclass
class RadialGradient(Element, _Gradient, m.Color, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/radialGradient
    """
    element_name = "radialGradient"
    cx: Length | Number | None = None
    cy: Length | Number | None = None
    r: Length | Number | None = None
    fr: Length | Number | None = None
    fx: Length | Number | None = None
    fy: Length | Number | None = None


@dataclass
class Stop(Element, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/stop
    """
    element_name = "stop"
    offset: Length | Number | None = None
    stop_opacity: Optional[Number] = None
    stop_color: Optional[str] = None
    class_: Optional[list[str]] = None


@dataclass
class Pattern(Element, m.Color, m.GraphicsElementEvents, m.Graphics):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/pattern
    """
    element_name = "pattern"
    externalResourcesRequired: Optional[bool] = None
    viewBox: Optional[ViewBoxSpec] = None
    preserveAspectRatio: Optional[PreserveAspectRatio] = None
    patternUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    patternTransform: Optional[list[Transform]] = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    patternContentUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    href: Optional[str] = None
    class_: Optional[list[str]] = None
    mask: Optional[str] = None
    clip_path: Optional[str] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class ClipPath(Element, m.Color, m.Graphics):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/clipPath
    """
    element_name = "clipPath"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    clipPathUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    class_: Optional[list[str]] = None
    mask: Optional[str] = None
    clip_path: Optional[str] = None


@dataclass
class Mask(Element, m.Color, m.Graphics):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/mask
    """
    element_name = "mask"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    maskUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    maskContentUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    class_: Optional[list[str]] = None
    mask: Optional[str] = None
    clip_path: Optional[str] = None


@dataclass
class A(Element, m.Color, m.GraphicsElementEvents, m.Graphics):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/a
    """
    element_name = "a"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    target: Optional[Literal["_self", "_parent", "_top", "_blank"]] = None
    href: Optional[str] = None
    class_: Optional[list[str]] = None
    visibility: Optional[Literal["visible", "hidden", "inherit"]] = None
    mask: Optional[str] = None
    opacity: Optional[Number] = None
    clip_path: Optional[str] = None


@dataclass
class View(Element, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/view
    """
    element_name = "view"
    externalResourcesRequired: Optional[bool] = None
    viewBox: Optional[ViewBoxSpec] = None
    preserveAspectRatio: Optional[PreserveAspectRatio] = None


@dataclass
class Script(Element, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/script
    """
    element_name = "script"
    externalResourcesRequired: Optional[bool] = None
    type: Optional[str] = None
    href: Optional[str] = None


@dataclass
class Animate(Element, m.Animation, m.Color, m.AnimationTiming, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/animate
    """
    element_name = "animate"
    externalResourcesRequired: Optional[bool] = None
    keyPoints: Optional[str] = None
    attributeName: Optional[str] = None


@dataclass
class Set(Element, m.AnimationTiming, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/set
    """
    element_name = "set"
    externalResourcesRequired: Optional[bool] = None
    to: Optional[str] = None
    min: Optional[str] = None
    keyPoints: Optional[str] = None
    attributeName: Optional[str] = None
    href: Optional[str] = None


@dataclass
class AnimateMotion(Element, m.Animation, m.AnimationTiming, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/animateMotion
    """
    element_name = "animateMotion"
    externalResourcesRequired: Optional[bool] = None
    path: Optional[str] = None
    keyPoints: Optional[str] = None
    rotate: Optional[str] = None
    origin: Optional[str] = None


@dataclass
class MPath(Element, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/mpath
    """
    element_name = "mpath"
    externalResourcesRequired: Optional[bool] = None
    href: Optional[str] = None


@dataclass
class AnimateTransform(Element, m.Animation, m.AnimationTiming, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/animateTransform
    """
    element_name = "animateTransform"
    externalResourcesRequired: Optional[bool] = None
    type: Optional[Literal["translate", "scale", "rotate", "skewX", "skewY"]] = None
    keyPoints: Optional[str] = None
    attributeName: Optional[str] = None


@dataclass
class DefinitionSrc(Element):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/definition
    """
    element_name = "definition-src"
    pass


@dataclass
class Metadata(Element, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/metadata
    """
    element_name = "metadata"
    pass


@dataclass
class ForeignObject(Element, m.Color, m.GraphicsElementEvents, m.Graphics):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/foreignObject
    """
    element_name = "foreignObject"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[list[Transform]] = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    content: Optional[str] = None
    class_: Optional[list[str]] = None
    vector_effect: Optional[Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"]] = None
    visibility: Optional[Literal["visible", "hidden", "inherit"]] = None
    opacity: Optional[Number] = None
    overflow: Optional[Literal["visible", "hidden", "scroll", "auto", "inherit"]] = None


@dataclass
class Use(Element, m.GraphicsElementEvents, m.Color, m.Graphics, m.FillStroke):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/use
    """
    element_name = "use"
    href: Optional[str] = None
    class_: Optional[list[str]] = None
    style: Optional[str] = None
    transform: Optional[list[Transform]] = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    vector_effect: Optional[Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"]] = None
    opacity: Optional[Number] = None
    clip_path: Optional[str] = None
    mask: Optional[str] = None
    fill_rule: Optional[Literal["evenodd", "nonzero", "inherit"]] = None
    fill_opacity: Optional[Number] = None
    fill: Optional[str] = None
