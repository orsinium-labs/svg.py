from dataclasses import dataclass, asdict
from enum import Enum
from typing import Any, ClassVar, Dict, List, Optional, Union
from . import _mixins as m, values
from typing_extensions import Literal


@dataclass
class Element:
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/Core
    """

    element_name: ClassVar[str]

    id: Optional[str] = None
    tabindex: Optional[int] = None
    lang: Optional[str] = None
    xml__lang: Optional[str] = None

    transform_origin: Optional[str] = None

    # https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/Styling
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None

    @classmethod
    def _as_str(cls, val: Any) -> str:
        if val is None:
            return ""
        if isinstance(val, Element):
            return str(val)
        if isinstance(val, Enum):
            return val.value
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
        elements: Optional[List[Element]]
        elements = getattr(self, "elements", None)
        if elements:
            content = "".join(self._as_str(e) for e in elements)
            return f"<{self.element_name} {props}>{content}</{self.element_name}>"
        return f"<{self.element_name} {props}/>"

    def __str__(self) -> str:
        return self.as_str()


@dataclass
class SVG(
    Element,
    m.Presentation,
    m.GraphicsElementEvents,
    m.DocumentEvents,
):
    element_name = "svg"
    elements: Optional[List[Element]] = None
    viewBox: Optional[values.ViewBoxSpec] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class G(
    Element,
    m.Presentation,
    m.GraphicsElementEvents,
):
    element_name = "g"
    elements: Optional[List[Element]] = None
    transform: Optional[values.Transforms] = None


@dataclass
class Defs(
    Element,
    m.Presentation,
    m.GraphicsElementEvents,
):
    element_name = "defs"
    elements: Optional[List[Element]] = None
    transform: Optional[values.Transforms] = None


@dataclass
class Desc(Element):
    element_name = "desc"
    content: Optional[str] = None


@dataclass
class Title(Element):
    element_name = "title"
    content: Optional[str] = None


@dataclass
class Symbol(
    Element,
    m.Presentation,
    m.GraphicsElementEvents,
):
    element_name = "symbol"
    elements: Optional[List[Element]] = None
    viewBox: Optional[values.ViewBoxSpec] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    refX: Optional[values.Coordinate] = None
    refY: Optional[values.Coordinate] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class Image(
    Element,
    m.Color,
    m.Graphics,
    m.Viewports,
    m.GraphicsElementEvents,
):
    element_name = "image"
    href: Optional[str] = None
    transform: Optional[values.Transforms] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class Switch(Element, m.Color):
    element_name = "switch"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None


@dataclass
class Style(Element):
    element_name = "style"
    type: Optional[values.ContentType] = None
    media: Optional[values.MediaDesc] = None
    title: Optional[str] = None


@dataclass
class _FigElements:
    elements: Optional[
        List[
            Union[
                "Animate",
                "Set",
                "AnimateMotion",
                "AnimateTransform",
            ]
        ]
    ] = None
    pathLength: Optional[float] = None
    paint_order: Optional[Literal["normal", "fill", "stroke", "markers"]] = None


@dataclass
class Path(Element, _FigElements, m.Color):
    element_name = "path"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    d: Optional[List[values.PathData]] = None


@dataclass
class Rect(Element, _FigElements, m.Color):
    element_name = "rect"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    rx: Optional[values.Length] = None
    ry: Optional[values.Length] = None


@dataclass
class Circle(Element, _FigElements, m.Color):
    element_name = "circle"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    cx: Optional[values.Length] = None
    cy: Optional[values.Length] = None
    r: Optional[values.Length] = None


@dataclass
class Ellipse(Element, _FigElements, m.Color):
    element_name = "ellipse"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    cx: Optional[values.Length] = None
    cy: Optional[values.Length] = None
    rx: Optional[values.Length] = None
    ry: Optional[values.Length] = None


@dataclass
class Line(Element, _FigElements, m.Color):
    element_name = "line"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    x1: Optional[values.Coordinate] = None
    y1: Optional[values.Coordinate] = None
    x2: Optional[values.Coordinate] = None
    y2: Optional[values.Coordinate] = None


@dataclass
class Polyline(Element, _FigElements, m.Color):
    element_name = "polyline"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    points: Optional[values.Points] = None


@dataclass
class Polygon(Element, _FigElements, m.Color):
    element_name = "polygon"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    points: Optional[values.Points] = None


@dataclass
class Text(Element, m.FontSpecification, m.TextContentElements, m.Color):
    element_name = "text"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    dx: Optional[values.Coordinate] = None
    dy: Optional[values.Coordinate] = None
    rotate: Optional[values.Rotation] = None
    textLength: Optional[values.Length] = None
    lengthAdjust: Optional[Literal["spacing", "spacingAndGlyphs"]] = None


@dataclass
class TSpan(Element, m.FontSpecification, m.TextContentElements, m.Color):
    element_name = "tspan"
    externalResourcesRequired: Optional[bool] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    dx: Optional[values.Coordinate] = None
    dy: Optional[values.Coordinate] = None
    rotate: Optional[str] = None
    textLength: Optional[values.Length] = None
    lengthAdjust: Optional[Literal["spacing", "spacingAndGlyphs"]] = None


@dataclass
class TextPath(Element, m.FontSpecification, m.TextContentElements, m.Color):
    element_name = "textPath"
    elements: Optional[
        List[
            Union[
                "Desc",
                "Title",
                "Metadata",
                "TSpan",
                "A",
                "Animate",
                "Set",
            ]
        ]
    ] = None
    externalResourcesRequired: Optional[bool] = None
    startOffset: Optional[str] = None
    textLength: Optional[values.Length] = None
    lengthAdjust: Optional[Literal["spacing", "spacingAndGlyphs"]] = None
    method: Optional[Literal["align", "stretch"]] = None
    spacing: Optional[Literal["auto", "exact"]] = None
    href: Optional[str] = None
    path: Optional[str] = None
    side: Optional[values.Side] = None


@dataclass
class Marker(Element, m.Color):
    element_name = "marker"
    externalResourcesRequired: Optional[bool] = None
    viewBox: Optional[values.ViewBoxSpec] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    refX: Optional[values.Coordinate] = None
    refY: Optional[values.Coordinate] = None
    markerUnits: Optional[Any] = None
    markerWidth: Optional[values.Length] = None
    markerHeight: Optional[values.Length] = None
    orient: Optional[str] = None


@dataclass
class ColorProfile(Element):
    element_name = "color-profile"
    local: Optional[str] = None
    rendering_intent: Optional[Any] = None


@dataclass
class _Gradient:
    elements: Optional[List[Union["Stop", "Animate", "Set", "AnimateTransform"]]] = None
    externalResourcesRequired: Optional[bool] = None
    gradientUnits: Optional[Any] = None
    gradientTransform: Optional[Any] = None
    spreadMethod: Optional[Any] = None
    href: Optional[str] = None


@dataclass
class LinearGradient(Element, _Gradient, m.Color):
    element_name = "linearGradient"
    x1: Optional[values.Coordinate] = None
    y1: Optional[values.Coordinate] = None
    x2: Optional[values.Coordinate] = None
    y2: Optional[values.Coordinate] = None


@dataclass
class RadialGradient(Element, _Gradient, m.Color):
    element_name = "radialGradient"
    cx: Optional[values.Length] = None
    cy: Optional[values.Length] = None
    r: Optional[values.Length] = None
    fr: Optional[values.Length] = None
    fx: Optional[Any] = None
    fy: Optional[Any] = None


@dataclass
class Stop(Element):
    element_name = "stop"
    offset: Optional[values.Length] = None
    stop_opacity: Optional[values.Opacity] = None
    stop_color: Optional[values.SVGColor] = None


@dataclass
class Pattern(Element, m.Color):
    element_name = "pattern"
    externalResourcesRequired: Optional[bool] = None
    viewBox: Optional[Any] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    patternUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    patternTransform: Optional[Any] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    patternContentUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    href: Optional[str] = None


@dataclass
class ClipPath(Element, m.Color):
    element_name = "clipPath"
    elements: Optional[
        List[
            Union[
                "Path",
                "Text",
                "Rect",
                "Circle",
                "Ellipse",
                "Line",
                "Polyline",
                "Polygon",
                "Animate",
                "Set",
                "AnimateMotion",
                "AnimateTransform",
            ]
        ]
    ] = None
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    clipPathUnits: Optional[Any] = None


@dataclass
class Mask(Element, m.Color):
    element_name = "mask"
    elements: Optional[List[Element]] = None
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    maskUnits: Optional[Any] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    maskContentUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None


@dataclass
class A(Element, m.Color):
    element_name = "a"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    target: Optional[Any] = None
    href: Optional[str] = None


@dataclass
class View(Element):
    element_name = "view"
    externalResourcesRequired: Optional[bool] = None
    viewBox: Optional[Any] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None


@dataclass
class Script(Element):
    element_name = "script"
    externalResourcesRequired: Optional[bool] = None
    type: Optional[Any] = None
    href: Optional[str] = None


@dataclass
class Animate(Element, m.Animation, m.Color):
    element_name = "animate"
    externalResourcesRequired: Optional[bool] = None


@dataclass
class Set(Element):
    element_name = "set"
    externalResourcesRequired: Optional[bool] = None
    to: Optional[str] = None
    min: Optional[str] = None


@dataclass
class AnimateMotion(Element, m.Animation):
    element_name = "animateMotion"
    externalResourcesRequired: Optional[bool] = None
    path: Optional[str] = None
    keyPoints: Optional[str] = None
    rotate: Optional[str] = None
    origin: Optional[str] = None


@dataclass
class MPath(Element):
    element_name = "mpath"
    externalResourcesRequired: Optional[bool] = None
    pass


@dataclass
class AnimateTransform(Element, m.Animation):
    element_name = "animateTransform"
    externalResourcesRequired: Optional[bool] = None
    type: Optional[Literal["translate", "scale", "rotate", "skewX", "skewY"]] = None


@dataclass
class DefinitionSrc(Element):
    element_name = "definition-src"
    pass


@dataclass
class Metadata(Element):
    element_name = "metadata"
    pass


@dataclass
class ForeignObject(Element, m.Color):
    element_name = "foreignObject"
    externalResourcesRequired: Optional[bool] = None
    transform: Optional[values.Transforms] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    content: Optional[str] = None


@dataclass
class Use(
    Element,
    m.Presentation,
    m.GraphicsElementEvents,
):
    element_name = "use"
    elements: Optional[
        List[
            Union[
                "Set",
                "Animate",
                "AnimateMotion",
                "AnimateTransform",
            ]
        ]
    ] = None
    href: Optional[str] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class Cursor(Element):
    element_name = "cursor"
    externalResourcesRequired: Optional[bool] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
