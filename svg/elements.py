from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar
from datetime import timedelta, datetime

from . import _mixins as m
from ._path import PathData
from ._transforms import Transform
from ._types import Length, Number, PreserveAspectRatio, ViewBoxSpec, to_clock_value, to_wallclock_sync_value


if TYPE_CHECKING:
    from typing_extensions import Literal


# Attributes whose elements should be separated by a semicolon (;) rather than a space.
_SEMICOLON_ATTRS = frozenset({
    "values",
    "keyTimes",
    "keySplines",
    "keyPoints",
    "begin",
    "end",
})
_SEMICOLON_TYPES = frozenset({
    m.Animation,
    m.AnimationTiming,
})


@dataclass
class Element:
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/Core
    """

    element_name: ClassVar[str]

    elements: list[Element] | None = None
    text: str | None = None
    id: str | None = None
    tabindex: int | None = None
    lang: str | None = None

    transform_origin: str | None = None
    style: str | None = None
    data: dict | None = None

    extra: dict[str, str] | None = None
    """Any extra attributes to add to the element.

    Useful for HTMX and other HTML frameworks. Use with caution.
    """

    @classmethod
    def _as_str(cls, val: Any, key: str | None = None) -> str:
        if val is None:
            return ""
        if isinstance(val, Element):
            return str(val)
        if isinstance(val, Enum):
            return val.value
        if isinstance(val, bool):
            return str(val).lower()
        if isinstance(val, (list, tuple)):
            sep = " "
            # Some attributes of some animation-related elements
            # use semicolon instead of space to separate list elements.
            if key in _SEMICOLON_ATTRS:
                if set(cls.__bases__) & _SEMICOLON_TYPES:
                    sep = ";"
            return sep.join(cls._as_str(v) for v in val)
        if isinstance(val, timedelta):
            return to_clock_value(val)
        if isinstance(val, datetime):
            return to_wallclock_sync_value(val)
        return str(val)

    def as_dict(self) -> dict[str, str]:
        result = {}
        for key, val in vars(self).items():
            if val is None:
                continue
            if key in ("elements", "text", "data", "attributes"):
                continue
            key = key.rstrip("_")
            key = key.replace("__", ":")
            key = key.replace("_", "-")
            result[key] = self._as_str(val, key=key)
        return result

    def as_str(self) -> str:
        props = " ".join(f'{k}="{v}"' for k, v in self.as_dict().items())
        if self.data:
            if props:
                props += " "
            props += " ".join(f'data-{k}="{v}"' for k, v in self.data.items())
        if self.extra:
            if props:
                props += " "
            props += " ".join(f'{k}="{v}"' for k, v in self.extra.items())
        if props:
            props = " " + props
        if self.text:
            return f"<{self.element_name}{props}>{self.text}</{self.element_name}>"
        if self.elements:
            content = "".join(self._as_str(e) for e in self.elements)
            return f"<{self.element_name}{props}>{content}</{self.element_name}>"
        return f"<{self.element_name}{props}/>"

    def __str__(self) -> str:
        return self.as_str()

    def _repr_svg_(self) -> str:
        """Used by Jupyter Notebook for rich display.
        """
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
    xmlns: str | None = "http://www.w3.org/2000/svg"
    viewBox: ViewBoxSpec | None = None
    preserveAspectRatio: PreserveAspectRatio | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    class_: list[str] | None = None
    mask: str | None = None
    opacity: Number | None = None
    clip_path: str | None = None
    overflow: Literal["visible", "hidden", "scroll", "auto", "inherit"] | None = None

    onunload: str | None = None
    onabort: str | None = None
    onerror: str | None = None
    onresize: str | None = None
    onscroll: str | None = None
    onzoom: str | None = None


@dataclass
class G(
    Element,
    m.GraphicsElementEvents,
    m.Color,
    m.Graphics,
    m.FillStroke,
):
    """The <g> SVG element is a container used to group other SVG elements.

    Transformations applied to the <g> element are performed on its child elements,
    and its attributes are inherited by its children. It can also group multiple elements
    to be referenced later with the <use> element.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/g
    """
    element_name = "g"
    transform: list[Transform] | None = None
    class_: list[str] | None = None
    mask: str | None = None
    opacity: Number | None = None
    clip_path: str | None = None
    fill_rule: Literal["evenodd", "nonzero", "inherit"] | None = None
    fill_opacity: Number | None = None
    fill: str | None = None


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
    transform: list[Transform] | None = None
    class_: list[str] | None = None
    pointer_events: str | None = None  # TODO


@dataclass
class Desc(Element, m.GraphicsElementEvents):
    """The <desc> element provides an accessible, long-text description of any element.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/desc
    """
    element_name = "desc"
    content: str | None = None
    class_: list[str] | None = None


@dataclass
class Title(Element, m.GraphicsElementEvents):
    """The <title> element provides an accessible, short-text description of any element.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/title
    """
    element_name = "title"
    content: str | None = None
    class_: list[str] | None = None


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
    viewBox: ViewBoxSpec | None = None
    preserveAspectRatio: PreserveAspectRatio | None = None
    refX: Length | Number | None = None
    refY: Length | Number | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    class_: list[str] | None = None
    mask: str | None = None
    opacity: Number | None = None
    clip_path: str | None = None
    overflow: Literal["visible", "hidden", "scroll", "auto", "inherit"] | None = None


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
    href: str | None = None
    transform: list[Transform] | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    preserveAspectRatio: PreserveAspectRatio | None = None
    image_rendering: Literal["auto", "optimizeSpeed", "optimizeQuality"] | None = None
    class_: list[str] | None = None
    vector_effect: Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"] | None = None
    visibility: Literal["visible", "hidden", "inherit"] | None = None
    mask: str | None = None
    opacity: Number | None = None
    clip_path: str | None = None
    overflow: Literal["visible", "hidden", "scroll", "auto", "inherit"] | None = None


@dataclass
class Switch(Element, m.Color, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/switch
    """
    element_name = "switch"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    opacity: Number | None = None
    class_: list[str] | None = None
    pointer_events: str | None = None  # TODO


@dataclass
class Style(Element, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/style
    """
    element_name = "style"
    type: str | None = None
    media: list[str] | None = None
    title: str | None = None


@dataclass
class _FigureElement(m.Color, m.GraphicsElementEvents, m.Graphics, m.FillStroke):
    pathLength: float | None = None
    paint_order: Literal["normal", "fill", "stroke", "markers"] | None = None
    shape_rendering: Literal["auto", "optimizeSpeed", "crispEdges", "geometricPrecision", "inherit"] | None = None
    class_: list[str] | None = None
    vector_effect: Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"] | None = None
    visibility: Literal["visible", "hidden", "inherit"] | None = None
    mask: str | None = None
    opacity: Number | None = None
    clip_path: str | None = None


@dataclass
class Path(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/path
    """
    element_name = "path"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    d: list[PathData] | None = None
    marker_start: str | None = None
    marker_mid: str | None = None
    marker_end: str | None = None
    stroke_linecap: Literal["butt", "round", "square", "inherit"] | None = None
    stroke_linejoin: Literal["miter", "round", "bevel", "inherit"] | None = None
    stroke_miterlimit: Number | None = None
    fill_rule: Literal["evenodd", "nonzero", "inherit"] | None = None
    fill_opacity: Number | None = None
    fill: str | None = None


@dataclass
class Rect(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/rect
    """
    element_name = "rect"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    rx: Length | Number | None = None
    ry: Length | Number | None = None
    marker_start: str | None = None
    marker_mid: str | None = None
    marker_end: str | None = None
    stroke_linejoin: Literal["miter", "round", "bevel", "inherit"] | None = None
    stroke_miterlimit: Number | None = None
    fill_opacity: Number | None = None
    fill: str | None = None


@dataclass
class Circle(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/circle
    """
    element_name = "circle"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    cx: Length | Number | None = None
    cy: Length | Number | None = None
    r: Length | Number | None = None
    marker_mid: str | None = None
    fill_opacity: Number | None = None
    fill: str | None = None


@dataclass
class Ellipse(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/ellipse
    """
    element_name = "ellipse"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    cx: Length | Number | None = None
    cy: Length | Number | None = None
    rx: Length | Number | None = None
    ry: Length | Number | None = None
    marker_start: str | None = None
    marker_mid: str | None = None
    marker_end: str | None = None
    fill_opacity: Number | None = None
    fill: str | None = None


@dataclass
class Line(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/line
    """
    element_name = "line"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    x1: Length | Number | None = None
    y1: Length | Number | None = None
    x2: Length | Number | None = None
    y2: Length | Number | None = None
    marker_start: str | None = None
    marker_mid: str | None = None
    marker_end: str | None = None
    stroke_linecap: Literal["butt", "round", "square", "inherit"] | None = None


@dataclass
class Polyline(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/polyline
    """
    element_name = "polyline"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    points: list[Number] | None = None
    marker_start: str | None = None
    marker_mid: str | None = None
    marker_end: str | None = None
    stroke_linecap: Literal["butt", "round", "square", "inherit"] | None = None
    stroke_linejoin: Literal["miter", "round", "bevel", "inherit"] | None = None
    stroke_miterlimit: Number | None = None
    fill_rule: Literal["evenodd", "nonzero", "inherit"] | None = None
    fill_opacity: Number | None = None
    fill: str | None = None


@dataclass
class Polygon(Element, _FigureElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/polygon
    """
    element_name = "polygon"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    points: list[Number] | None = None
    marker_start: str | None = None
    marker_mid: str | None = None
    marker_end: str | None = None
    stroke_linejoin: Literal["miter", "round", "bevel", "inherit"] | None = None
    stroke_miterlimit: Number | None = None
    fill_rule: Literal["evenodd", "nonzero", "inherit"] | None = None
    fill_opacity: Number | None = None
    fill: str | None = None


@dataclass
class _TextElement(
    m.FontSpecification,
    m.TextContentElements,
    m.Color,
    m.GraphicsElementEvents,
    m.Graphics,
    m.FillStroke,
):
    paint_order: Literal["normal", "fill", "stroke", "markers"] | None = None
    class_: list[str] | None = None
    vector_effect: Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"] | None = None
    visibility: Literal["visible", "hidden", "inherit"] | None = None
    fill_opacity: Number | None = None
    fill: str | None = None


@dataclass
class Text(Element, _TextElement):
    """The SVG <text> element draws a graphics element consisting of text.

    It's possible to apply a gradient, pattern, clipping path, mask, or filter to <text>,
    like any other SVG graphics element.

    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/text
    """
    element_name = "text"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    dx: Length | Number | None = None
    dy: Length | Number | None = None
    textLength: Length | Number | None = None
    lengthAdjust: Literal["spacing", "spacingAndGlyphs"] | None = None
    writing_mode: Literal["horizontal-tb", "vertical-rl", "vertical-lr"] | None = None
    text_rendering: Literal["auto", "optimizeSpeed", "optimizeLegibility", "geometricPrecision"] | None = None
    stroke_linecap: Literal["butt", "round", "square", "inherit"] | None = None
    stroke_linejoin: Literal["miter", "round", "bevel", "inherit"] | None = None
    stroke_miterlimit: Number | None = None
    fill_rule: Literal["evenodd", "nonzero", "inherit"] | None = None
    mask: str | None = None
    opacity: Number | None = None
    clip_path: str | None = None
    overflow: Literal["visible", "hidden", "scroll", "auto", "inherit"] | None = None


@dataclass
class TSpan(Element, _TextElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/tspan
    """
    element_name = "tspan"
    externalResourcesRequired: bool | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    dx: Length | Number | None = None
    dy: Length | Number | None = None
    textLength: Length | Number | None = None
    lengthAdjust: Literal["spacing", "spacingAndGlyphs"] | None = None
    writing_mode: Literal["horizontal-tb", "vertical-rl", "vertical-lr"] | None = None
    alignment_baseline: None | Literal[
        "baseline", "top", "before-edge", "text-top",
        "text-before-edge", "middle", "bottom",
        "after-edge", "text-bottom", "text-after-edge", "ideographic",
        "lower", "hanging", "mathematical", "inherit",
    ] = None
    baseline_shift: Literal["baseline", "sub", "super", "inherit"] | None = None
    stroke_linecap: Literal["butt", "round", "square", "inherit"] | None = None
    stroke_linejoin: Literal["miter", "round", "bevel", "inherit"] | None = None
    stroke_miterlimit: Number | None = None
    fill_rule: Literal["evenodd", "nonzero", "inherit"] | None = None
    opacity: Number | None = None


@dataclass
class TextPath(Element, _TextElement):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/textPath
    """
    element_name = "textPath"
    externalResourcesRequired: bool | None = None
    startOffset: str | None = None
    textLength: Length | Number | None = None
    lengthAdjust: Literal["spacing", "spacingAndGlyphs"] | None = None
    method: Literal["align", "stretch"] | None = None
    spacing: Literal["auto", "exact"] | None = None
    href: str | None = None
    path: str | None = None
    side: Literal["left", "right"] | None = None
    writing_mode: Literal["horizontal-tb", "vertical-rl", "vertical-lr"] | None = None
    alignment_baseline: None | Literal[
        "baseline", "top", "before-edge", "text-top",
        "text-before-edge", "middle", "bottom",
        "after-edge", "text-bottom", "text-after-edge", "ideographic",
        "lower", "hanging", "mathematical", "inherit",
    ] = None
    baseline_shift: Literal["baseline", "sub", "super", "inherit"] | None = None
    stroke_linecap: Literal["butt", "round", "square", "inherit"] | None = None
    stroke_linejoin: Literal["miter", "round", "bevel", "inherit"] | None = None
    stroke_miterlimit: Number | None = None
    fill_rule: Literal["evenodd", "nonzero", "inherit"] | None = None
    opacity: Number | None = None


@dataclass
class Marker(Element, m.Color, m.GraphicsElementEvents, m.Graphics):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/marker
    """
    element_name = "marker"
    externalResourcesRequired: bool | None = None
    viewBox: ViewBoxSpec | None = None
    preserveAspectRatio: PreserveAspectRatio | None = None
    refX: Length | Number | None = None
    refY: Length | Number | None = None
    markerUnits: Literal["strokeWidth", "userSpaceOnUse", "userSpace"] | None = None
    markerWidth: Length | Number | None = None
    markerHeight: Length | Number | None = None
    orient: str | None = None
    opacity: Number | None = None
    clip_path: str | None = None
    class_: list[str] | None = None
    mask: str | None = None
    overflow: Literal["visible", "hidden", "scroll", "auto", "inherit"] | None = None


@dataclass
class ColorProfile(Element):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/color
    """
    element_name = "color-profile"
    local: str | None = None


@dataclass
class _Gradient:
    externalResourcesRequired: bool | None = None
    gradientUnits: Literal["userSpaceOnUse", "objectBoundingBox"] | None = None
    gradientTransform: list[Transform] | None = None
    spreadMethod: Literal["pad", "reflect", "repeat"] | None = None
    href: str | None = None
    class_: list[str] | None = None


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
    stop_opacity: Number | None = None
    stop_color: str | None = None
    class_: list[str] | None = None


@dataclass
class Pattern(Element, m.Color, m.GraphicsElementEvents, m.Graphics):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/pattern
    """
    element_name = "pattern"
    externalResourcesRequired: bool | None = None
    viewBox: ViewBoxSpec | None = None
    preserveAspectRatio: PreserveAspectRatio | None = None
    patternUnits: Literal["userSpaceOnUse", "objectBoundingBox"] | None = None
    patternTransform: list[Transform] | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    patternContentUnits: Literal["userSpaceOnUse", "objectBoundingBox"] | None = None
    href: str | None = None
    class_: list[str] | None = None
    mask: str | None = None
    clip_path: str | None = None
    overflow: Literal["visible", "hidden", "scroll", "auto", "inherit"] | None = None


@dataclass
class ClipPath(Element, m.Color, m.Graphics):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/clipPath
    """
    element_name = "clipPath"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    clipPathUnits: Literal["userSpaceOnUse", "objectBoundingBox"] | None = None
    class_: list[str] | None = None
    mask: str | None = None
    clip_path: str | None = None


@dataclass
class Mask(Element, m.Color, m.Graphics):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/mask
    """
    element_name = "mask"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    maskUnits: Literal["userSpaceOnUse", "objectBoundingBox"] | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    maskContentUnits: Literal["userSpaceOnUse", "objectBoundingBox"] | None = None
    class_: list[str] | None = None
    mask: str | None = None
    clip_path: str | None = None


@dataclass
class A(Element, m.Color, m.GraphicsElementEvents, m.Graphics):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/a
    """
    element_name = "a"
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    target: Literal["_self", "_parent", "_top", "_blank"] | None = None
    href: str | None = None
    class_: list[str] | None = None
    visibility: Literal["visible", "hidden", "inherit"] | None = None
    mask: str | None = None
    opacity: Number | None = None
    clip_path: str | None = None


@dataclass
class View(Element, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/view
    """
    element_name = "view"
    externalResourcesRequired: bool | None = None
    viewBox: ViewBoxSpec | None = None
    preserveAspectRatio: PreserveAspectRatio | None = None


@dataclass
class Script(Element, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/script
    """
    element_name = "script"
    externalResourcesRequired: bool | None = None
    type: str | None = None
    href: str | None = None


@dataclass
class Animate(Element, m.Animation, m.Color, m.AnimationTiming, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/animate
    """
    element_name = "animate"
    externalResourcesRequired: bool | None = None
    attributeName: str | None = None


@dataclass
class Set(Element, m.AnimationTiming, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/set
    """
    element_name = "set"
    externalResourcesRequired: bool | None = None
    to: str | None = None
    attributeName: str | None = None
    href: str | None = None


@dataclass
class AnimateMotion(Element, m.Animation, m.AnimationTiming, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/animateMotion
    """
    element_name = "animateMotion"
    externalResourcesRequired: bool | None = None
    path: list[PathData] | None = None
    rotate: Number | Literal["auto", "auto-reverse"] | None = None
    origin: Literal["default"] | None = None


@dataclass
class MPath(Element, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/mpath
    """
    element_name = "mpath"
    externalResourcesRequired: bool | None = None
    href: str | None = None


@dataclass
class AnimateTransform(Element, m.Animation, m.AnimationTiming, m.GraphicsElementEvents):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/animateTransform
    """
    element_name = "animateTransform"
    externalResourcesRequired: bool | None = None
    type: Literal["translate", "scale", "rotate", "skewX", "skewY"] | None = None
    attributeName: str | None = None


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
    externalResourcesRequired: bool | None = None
    transform: list[Transform] | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    content: str | None = None
    class_: list[str] | None = None
    vector_effect: Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"] | None = None
    visibility: Literal["visible", "hidden", "inherit"] | None = None
    opacity: Number | None = None
    overflow: Literal["visible", "hidden", "scroll", "auto", "inherit"] | None = None


@dataclass
class Use(Element, m.GraphicsElementEvents, m.Color, m.Graphics, m.FillStroke):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/use
    """
    element_name = "use"
    href: str | None = None
    class_: list[str] | None = None
    style: str | None = None
    transform: list[Transform] | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    vector_effect: Literal["none", "non-scaling-stroke", "non-scaling-size", "non-rotation", "fixed-position"] | None = None
    opacity: Number | None = None
    clip_path: str | None = None
    mask: str | None = None
    fill_rule: Literal["evenodd", "nonzero", "inherit"] | None = None
    fill_opacity: Number | None = None
    fill: str | None = None
