from dataclasses import dataclass, asdict
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from . import _mixins as m, values, enums


class Element:
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/Core
    """
    element_name: str

    id: Optional[str] = None
    tabindex: Optional[int] = None
    xml__base: Optional[str] = None
    xml__lang: Optional[str] = None

    @classmethod
    def _as_str(cls, val: Any) -> str:
        if val is None:
            return ''
        if isinstance(val, Element):
            return str(val)
        if isinstance(val, Enum):
            return val.value
        if isinstance(val, (list, tuple)):
            return ','.join(cls._as_str(v) for v in val)
        return str(val)

    def as_dict(self) -> Dict[str, str]:
        result = {}
        for key, val in asdict(self).items():
            if val is None:
                continue
            if key == 'elements':
                continue
            key = key.rstrip('_')
            key = key.replace('__', ':')
            key = key.replace('_', '-')
            result[key] = self._as_str(val)
        return result

    def as_str(self) -> str:
        props = ' '.join(f'{k}="{v}"' for k, v in self.as_dict().items())
        elements: Optional[List[Element]]
        elements = getattr(self, 'elements', None)
        if elements:
            content = ''.join(self._as_str(e) for e in elements)
            return f'<{self.element_name} {props}>{content}</{self.element_name}>'
        return f'<{self.element_name} {props}/>'

    def __str__(self) -> str:
        return self.as_str()


@dataclass
class SVG(
    Element,
    m.Presentation,
    m.GraphicsElementEvents,
    m.DocumentEvents,
):
    element_name = 'svg'
    elements: Optional[List[Element]] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    viewBox: Optional[values.ViewBoxSpec] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    zoomAndPan: Optional[enums.ZoomAndPan] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    contentScriptType: Optional[str] = None
    contentStyleType: Optional[str] = None


@dataclass
class G(
    Element,
    m.Presentation,
    m.GraphicsElementEvents,
):
    element_name = "g"
    elements: Optional[List[Element]] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None


@dataclass
class Defs(
    Element,
    m.Presentation,
    m.GraphicsElementEvents,
):
    element_name = "defs"
    elements: Optional[List[Element]] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None


@dataclass
class Desc(Element):
    element_name = "desc"
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    content: Optional[str] = None


@dataclass
class Title(Element):
    element_name = "title"
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    content: Optional[str] = None


@dataclass
class Symbol(
    Element,
    m.Presentation,
    m.GraphicsElementEvents,
):
    element_name = "symbol"
    elements: Optional[List[Element]] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
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
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class Switch(Element):
    element_name = "switch"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None


@dataclass
class Style(Element):
    element_name = "style"
    type: Optional[values.ContentType] = None
    media: Optional[values.MediaDesc] = None
    title: Optional[str] = None


@dataclass
class _FigElements:
    elements: Optional[List[Union[
        'Animate', 'Set', 'AnimateMotion', 'AnimateColor', 'AnimateTransform',
    ]]] = None
    pathLength: Optional[float] = None


@dataclass
class Path(Element, _FigElements):
    element_name = "path"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    d: Optional[List[values.PathData]] = None


@dataclass
class Rect(Element, _FigElements):
    element_name = "rect"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    rx: Optional[values.Length] = None
    ry: Optional[values.Length] = None


@dataclass
class Circle(Element, _FigElements):
    element_name = "circle"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    cx: Optional[values.Length] = None
    cy: Optional[values.Length] = None
    r: Optional[values.Length] = None


@dataclass
class Ellipse(Element, _FigElements):
    element_name = "ellipse"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    cx: Optional[values.Length] = None
    cy: Optional[values.Length] = None
    rx: Optional[values.Length] = None
    ry: Optional[values.Length] = None


@dataclass
class Line(Element, _FigElements):
    element_name = "line"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    x1: Optional[values.Coordinate] = None
    y1: Optional[values.Coordinate] = None
    x2: Optional[values.Coordinate] = None
    y2: Optional[values.Coordinate] = None


@dataclass
class Polyline(Element, _FigElements):
    element_name = "polyline"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    points: Optional[values.Points] = None


@dataclass
class Polygon(Element, _FigElements):
    element_name = "polygon"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    points: Optional[values.Points] = None


@dataclass
class Text(Element):
    element_name = "text"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    dx: Optional[values.Coordinate] = None
    dy: Optional[values.Coordinate] = None
    rotate: Optional[values.Rotation] = None
    textLength: Optional[values.Length] = None
    lengthAdjust: Optional[enums.LengthAdjust] = None


@dataclass
class TSpan(Element):
    element_name = "tspan"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    dx: Optional[values.Coordinate] = None
    dy: Optional[values.Coordinate] = None
    rotate: Optional[str] = None
    textLength: Optional[values.Length] = None
    lengthAdjust: Optional[enums.LengthAdjust] = None


@dataclass
class TextPath(Element):
    element_name = "textPath"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    startOffset: Optional[str] = None
    textLength: Optional[values.Length] = None
    lengthAdjust: Optional[enums.LengthAdjust] = None
    method: Optional[enums.TextPathMethod] = None
    spacing: Optional[enums.TextSpacing] = None


@dataclass
class AltGlyph(Element):
    element_name = "altGlyph"
    glyphRef: Optional[str] = None
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    dx: Optional[values.Coordinate] = None
    dy: Optional[values.Coordinate] = None
    rotate: Optional[str] = None


@dataclass
class AltGlyphDef(Element):
    element_name = "altGlyphDef"
    pass


@dataclass
class AltGlyphItem(Element):
    element_name = "altGlyphItem"
    pass


@dataclass
class GlyphRef(Element):
    element_name = "glyphRef"
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    glyphRef: Optional[str] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    dx: Optional[values.Coordinate] = None
    dy: Optional[values.Coordinate] = None


@dataclass
class Marker(Element):
    element_name = "marker"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
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
    elements: Optional[List[Union['Stop', 'Animate', 'Set', 'AnimateTransform']]] = None
    externalResourcesRequired: Optional[bool] = None
    gradientUnits: Optional[Any] = None
    gradientTransform: Optional[Any] = None
    spreadMethod: Optional[Any] = None


@dataclass
class LinearGradient(Element, _Gradient):
    element_name = "linearGradient"
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    x1: Optional[values.Coordinate] = None
    y1: Optional[values.Coordinate] = None
    x2: Optional[values.Coordinate] = None
    y2: Optional[values.Coordinate] = None


@dataclass
class RadialGradient(Element, _Gradient):
    element_name = "radialGradient"
    cx: Optional[values.Length] = None
    cy: Optional[values.Length] = None
    r: Optional[values.Length] = None
    fx: Optional[Any] = None
    fy: Optional[Any] = None


@dataclass
class Stop(Element):
    element_name = "stop"
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    offset: Optional[values.Length] = None
    stop_opacity: Optional[values.Opacity] = None
    stop_color: Optional[values.SVGColor] = None


@dataclass
class Pattern(Element):
    element_name = "pattern"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    viewBox: Optional[Any] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    patternUnits: Optional[enums.ContentUnits] = None
    patternTransform: Optional[Any] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    patternContentUnits: Optional[enums.ContentUnits] = None
    href: Optional[str] = None


@dataclass
class ClipPath(Element):
    element_name = "clipPath"
    elements: Optional[List[Union[
        'Path', 'Text', 'Rect', 'Circle', 'Ellipse', 'Line',
        'Polyline', 'Polygon', 'Animate', 'Set',
        'AnimateMotion', 'AnimateColor', 'AnimateTransform',
    ]]] = None
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    clipPathUnits: Optional[Any] = None


@dataclass
class Mask(Element):
    element_name = "mask"
    elements: Optional[List[Element]] = None
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    maskUnits: Optional[Any] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    maskContentUnits: Optional[enums.ContentUnits] = None


@dataclass
class A(Element):
    element_name = "a"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    target: Optional[Any] = None
    href: Optional[str] = None


@dataclass
class View(Element):
    element_name = "view"
    externalResourcesRequired: Optional[bool] = None
    viewBox: Optional[Any] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    zoomAndPan: Optional[Any] = None
    viewTarget: Optional[str] = None


@dataclass
class Script(Element):
    element_name = "script"
    externalResourcesRequired: Optional[bool] = None
    type: Optional[Any] = None
    href: Optional[str] = None


@dataclass
class Animate(Element):
    element_name = "animate"
    externalResourcesRequired: Optional[bool] = None


@dataclass
class Set(Element):
    element_name = "set"
    externalResourcesRequired: Optional[bool] = None
    to: Optional[str] = None


@dataclass
class AnimateMotion(Element):
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
class AnimateColor(Element):
    element_name = "animateColor"
    externalResourcesRequired: Optional[bool] = None
    pass


@dataclass
class AnimateTransform(Element):
    element_name = "animateTransform"
    externalResourcesRequired: Optional[bool] = None
    type: Optional[enums.TransformType] = None


@dataclass
class DefinitionSrc(Element):
    element_name = "definition-src"
    pass


@dataclass
class Metadata(Element):
    element_name = "metadata"
    pass


@dataclass
class ForeignObject(Element):
    element_name = "foreignObject"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    content: Optional[str] = None
