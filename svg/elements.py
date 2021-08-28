from dataclasses import dataclass, asdict
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from . import _mixins as m, values, enums


class Element:
    element_name: str

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
    m.StdAttrs,
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
    m.StdAttrs,
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
    m.StdAttrs,
    m.Presentation,
    m.GraphicsElementEvents,
):
    element_name = "defs"
    elements: Optional[List[Element]] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None


@dataclass
class Desc(Element, m.StdAttrs):
    element_name = "desc"
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    content: Optional[str] = None


@dataclass
class Title(Element, m.StdAttrs):
    element_name = "title"
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    content: Optional[str] = None


@dataclass
class Symbol(
    Element,
    m.StdAttrs,
    m.Presentation,
    m.GraphicsElementEvents,
):
    element_name = "symbol"
    elements: Optional[List[Element]] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    viewBox: Optional[values.ViewBoxSpec] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None


@dataclass
class Image(
    Element,
    m.StdAttrs,
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
class Switch(Element, m.StdAttrs):
    element_name = "switch"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None


@dataclass
class Style(Element, m.StdAttrs):
    element_name = "style"
    type: Optional[values.ContentType] = None
    media: Optional[values.MediaDesc] = None
    title: Optional[str] = None


@dataclass
class _FigElements:
    elements: Optional[List[Union[
        'Animate', 'Set', 'AnimateMotion', 'AnimateColor', 'AnimateTransform',
    ]]] = None


@dataclass
class Path(Element, m.StdAttrs, _FigElements):
    element_name = "path"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    d: Optional[List[values.PathData]] = None
    pathLength: Optional[float] = None


@dataclass
class Rect(Element, m.StdAttrs, _FigElements):
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
class Circle(Element, m.StdAttrs, _FigElements):
    element_name = "circle"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    cx: Optional[values.Length] = None
    cy: Optional[values.Length] = None
    r: Optional[values.Length] = None


@dataclass
class Ellipse(Element, m.StdAttrs, _FigElements):
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
class Line(Element, m.StdAttrs, _FigElements):
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
class Polyline(Element, m.StdAttrs, _FigElements):
    element_name = "polyline"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    points: Optional[values.Points] = None


@dataclass
class Polygon(Element, m.StdAttrs, _FigElements):
    element_name = "polygon"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    points: Optional[values.Points] = None


@dataclass
class Text(Element, m.StdAttrs):
    element_name = "text"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    textLength: Optional[values.Length] = None
    lengthAdjust: Optional[enums.LengthAdjust] = None


@dataclass
class TSpan(Element, m.StdAttrs):
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
class TextPath(Element, m.StdAttrs):
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
class AltGlyph(Element, m.StdAttrs):
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
class AltGlyphDef(Element, m.StdAttrs):
    element_name = "altGlyphDef"
    pass


@dataclass
class AltGlyphItem(Element, m.StdAttrs):
    element_name = "altGlyphItem"
    pass


@dataclass
class GlyphRef(Element, m.StdAttrs):
    element_name = "glyphRef"
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    glyphRef: Optional[str] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    dx: Optional[values.Coordinate] = None
    dy: Optional[values.Coordinate] = None


@dataclass
class Marker(Element, m.StdAttrs):
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
class ColorProfile(Element, m.StdAttrs):
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
class LinearGradient(Element, m.StdAttrs, _Gradient):
    element_name = "linearGradient"
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    x1: Optional[values.Coordinate] = None
    y1: Optional[values.Coordinate] = None
    x2: Optional[values.Coordinate] = None
    y2: Optional[values.Coordinate] = None


@dataclass
class RadialGradient(Element, m.StdAttrs, _Gradient):
    element_name = "radialGradient"
    cx: Optional[values.Length] = None
    cy: Optional[values.Length] = None
    r: Optional[values.Length] = None
    fx: Optional[Any] = None
    fy: Optional[Any] = None


@dataclass
class Stop(Element, m.StdAttrs):
    element_name = "stop"
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    offset: Optional[values.Length] = None


@dataclass
class Pattern(Element, m.StdAttrs):
    element_name = "pattern"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    viewBox: Optional[Any] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    patternUnits: Optional[Any] = None
    patternTransform: Optional[Any] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


@dataclass
class ClipPath(Element, m.StdAttrs):
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
class Mask(Element, m.StdAttrs):
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


@dataclass
class A(Element, m.StdAttrs):
    element_name = "a"
    externalResourcesRequired: Optional[bool] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    target: Optional[Any] = None


@dataclass
class View(Element, m.StdAttrs):
    element_name = "view"
    externalResourcesRequired: Optional[bool] = None
    viewBox: Optional[Any] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    zoomAndPan: Optional[Any] = None
    viewTarget: Optional[str] = None


@dataclass
class Script(Element, m.StdAttrs):
    element_name = "script"
    externalResourcesRequired: Optional[bool] = None
    type: Optional[Any] = None


@dataclass
class Animate(Element, m.StdAttrs):
    element_name = "animate"
    externalResourcesRequired: Optional[bool] = None


@dataclass
class Set(Element, m.StdAttrs):
    element_name = "set"
    externalResourcesRequired: Optional[bool] = None
    to: Optional[str] = None


@dataclass
class AnimateMotion(Element, m.StdAttrs):
    element_name = "animateMotion"
    externalResourcesRequired: Optional[bool] = None
    path: Optional[str] = None
    keyPoints: Optional[str] = None
    rotate: Optional[str] = None
    origin: Optional[str] = None


@dataclass
class MPath(Element, m.StdAttrs):
    element_name = "mpath"
    externalResourcesRequired: Optional[bool] = None
    pass


@dataclass
class AnimateColor(Element, m.StdAttrs):
    element_name = "animateColor"
    externalResourcesRequired: Optional[bool] = None
    pass


@dataclass
class AnimateTransform(Element, m.StdAttrs):
    element_name = "animateTransform"
    externalResourcesRequired: Optional[bool] = None
    type: Optional[enums.TransformType] = None


@dataclass
class DefinitionSrc(Element, m.StdAttrs):
    element_name = "definition-src"
    pass


@dataclass
class Metadata(Element, m.StdAttrs):
    element_name = "metadata"
    pass


@dataclass
class ForeignObject(Element, m.StdAttrs):
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
