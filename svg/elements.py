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
    version: Optional[str] = None


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
class Use(
    Element,
    m.StdAttrs,
    m.Presentation,
    m.GraphicsElementEvents,
):
    element_name = "use"
    elements: Optional[List[Union[
        'Set', 'Animate', 'AnimateMotion', 'AnimateColor', 'AnimateTransform',
    ]]] = None
    href: Optional[str] = None
    class_: Optional[values.Classes] = None
    style: Optional[values.StyleSheet] = None
    transform: Optional[values.Transforms] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None


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
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None


@dataclass
class Style(Element, m.StdAttrs):
    element_name = "style"
    type: Optional[Any] = None
    media: Optional[Any] = None
    title: Optional[Any] = None


@dataclass
class Path(Element, m.StdAttrs):
    element_name = "path"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    d: Optional[Any] = None
    pathLength: Optional[Any] = None


@dataclass
class Rect(Element, m.StdAttrs):
    element_name = "rect"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    x: Optional[Any] = None
    y: Optional[Any] = None
    width: Optional[Any] = None
    height: Optional[Any] = None
    rx: Optional[Any] = None
    ry: Optional[Any] = None


@dataclass
class Circle(Element, m.StdAttrs):
    element_name = "circle"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    cx: Optional[Any] = None
    cy: Optional[Any] = None
    r: Optional[Any] = None


@dataclass
class Ellipse(Element, m.StdAttrs):
    element_name = "ellipse"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    cx: Optional[Any] = None
    cy: Optional[Any] = None
    rx: Optional[Any] = None
    ry: Optional[Any] = None


@dataclass
class Line(Element, m.StdAttrs):
    element_name = "line"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    x1: Optional[Any] = None
    y1: Optional[Any] = None
    x2: Optional[Any] = None
    y2: Optional[Any] = None


@dataclass
class Polyline(Element, m.StdAttrs):
    element_name = "polyline"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    points: Optional[Any] = None


@dataclass
class Polygon(Element, m.StdAttrs):
    element_name = "polygon"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    points: Optional[Any] = None


@dataclass
class Text(Element, m.StdAttrs):
    element_name = "text"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    x: Optional[Any] = None
    y: Optional[Any] = None
    textLength: Optional[Any] = None
    lengthAdjust: Optional[Any] = None


@dataclass
class TSpan(Element, m.StdAttrs):
    element_name = "tspan"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    x: Optional[Any] = None
    y: Optional[Any] = None
    dx: Optional[Any] = None
    dy: Optional[Any] = None
    rotate: Optional[Any] = None
    textLength: Optional[Any] = None
    lengthAdjust: Optional[Any] = None


@dataclass
class TRef(Element, m.StdAttrs):
    element_name = "tref"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    x: Optional[Any] = None
    y: Optional[Any] = None
    dx: Optional[Any] = None
    dy: Optional[Any] = None
    rotate: Optional[Any] = None
    textLength: Optional[Any] = None
    lengthAdjust: Optional[Any] = None


@dataclass
class TextPath(Element, m.StdAttrs):
    element_name = "textPath"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    startOffset: Optional[Any] = None
    textLength: Optional[Any] = None
    lengthAdjust: Optional[Any] = None
    method: Optional[Any] = None
    spacing: Optional[Any] = None


@dataclass
class AltGlyph(Element, m.StdAttrs):
    element_name = "altGlyph"
    glyphRef: Optional[Any] = None
    format: Optional[Any] = None
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    x: Optional[Any] = None
    y: Optional[Any] = None
    dx: Optional[Any] = None
    dy: Optional[Any] = None
    rotate: Optional[Any] = None


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
    class_: Optional[Any] = None
    style: Optional[Any] = None
    glyphRef: Optional[Any] = None
    format: Optional[Any] = None
    x: Optional[Any] = None
    y: Optional[Any] = None
    dx: Optional[Any] = None
    dy: Optional[Any] = None


@dataclass
class Marker(Element, m.StdAttrs):
    element_name = "marker"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    viewBox: Optional[Any] = None
    preserveAspectRatio: Optional[Any] = None
    refX: Optional[Any] = None
    refY: Optional[Any] = None
    markerUnits: Optional[Any] = None
    markerWidth: Optional[Any] = None
    markerHeight: Optional[Any] = None
    orient: Optional[Any] = None


@dataclass
class ColorProfile(Element, m.StdAttrs):
    element_name = "color-profile"
    local: Optional[Any] = None
    name: Optional[Any] = None
    rendering_intent: Optional[Any] = None


@dataclass
class LinearGradient(Element, m.StdAttrs):
    element_name = "linearGradient"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    gradientUnits: Optional[Any] = None
    gradientTransform: Optional[Any] = None
    x1: Optional[Any] = None
    y1: Optional[Any] = None
    x2: Optional[Any] = None
    y2: Optional[Any] = None
    spreadMethod: Optional[Any] = None


@dataclass
class RadialGradient(Element, m.StdAttrs):
    element_name = "radialGradient"
    externalResourcesRequired: Optional[Any] = None
    gradientUnits: Optional[Any] = None
    gradientTransform: Optional[Any] = None
    cx: Optional[Any] = None
    cy: Optional[Any] = None
    r: Optional[Any] = None
    fx: Optional[Any] = None
    fy: Optional[Any] = None
    spreadMethod: Optional[Any] = None


@dataclass
class Stop(Element, m.StdAttrs):
    element_name = "stop"
    class_: Optional[Any] = None
    style: Optional[Any] = None
    offset: Optional[Any] = None


@dataclass
class Pattern(Element, m.StdAttrs):
    element_name = "pattern"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    viewBox: Optional[Any] = None
    preserveAspectRatio: Optional[Any] = None
    patternUnits: Optional[Any] = None
    patternTransform: Optional[Any] = None
    x: Optional[Any] = None
    y: Optional[Any] = None
    width: Optional[Any] = None
    height: Optional[Any] = None


@dataclass
class ClipPath(Element, m.StdAttrs):
    element_name = "clipPath"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    clipPathUnits: Optional[Any] = None


@dataclass
class Mask(Element, m.StdAttrs):
    element_name = "mask"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    maskUnits: Optional[Any] = None
    x: Optional[Any] = None
    y: Optional[Any] = None
    width: Optional[Any] = None
    height: Optional[Any] = None


@dataclass
class Cursor(Element, m.StdAttrs):
    element_name = "cursor"
    externalResourcesRequired: Optional[Any] = None
    x: Optional[Any] = None
    y: Optional[Any] = None


@dataclass
class A(Element, m.StdAttrs):
    element_name = "a"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    target: Optional[Any] = None


@dataclass
class View(Element, m.StdAttrs):
    element_name = "view"
    externalResourcesRequired: Optional[Any] = None
    viewBox: Optional[Any] = None
    preserveAspectRatio: Optional[Any] = None
    zoomAndPan: Optional[Any] = None
    viewTarget: Optional[Any] = None


@dataclass
class Script(Element, m.StdAttrs):
    element_name = "script"
    externalResourcesRequired: Optional[Any] = None
    type: Optional[Any] = None


@dataclass
class Animate(Element, m.StdAttrs):
    element_name = "animate"
    externalResourcesRequired: Optional[Any] = None


@dataclass
class Set(Element, m.StdAttrs):
    element_name = "set"
    externalResourcesRequired: Optional[Any] = None
    to: Optional[Any] = None


@dataclass
class AnimateMotion(Element, m.StdAttrs):
    element_name = "animateMotion"
    externalResourcesRequired: Optional[Any] = None
    path: Optional[Any] = None
    keyPoints: Optional[Any] = None
    rotate: Optional[Any] = None
    origin: Optional[Any] = None


@dataclass
class MPath(Element, m.StdAttrs):
    element_name = "mpath"
    externalResourcesRequired: Optional[Any] = None
    pass


@dataclass
class AnimateColor(Element, m.StdAttrs):
    element_name = "animateColor"
    externalResourcesRequired: Optional[Any] = None
    pass


@dataclass
class AnimateTransform(Element, m.StdAttrs):
    element_name = "animateTransform"
    externalResourcesRequired: Optional[Any] = None
    type: Optional[Any] = None


@dataclass
class Font(Element, m.StdAttrs):
    element_name = "font"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    horiz_origin_x: Optional[Any] = None
    horiz_origin_y: Optional[Any] = None
    horiz_adv_x: Optional[Any] = None
    vert_origin_x: Optional[Any] = None
    vert_origin_y: Optional[Any] = None
    vert_adv_y: Optional[Any] = None


@dataclass
class Glyph(Element, m.StdAttrs):
    element_name = "glyph"
    class_: Optional[Any] = None
    style: Optional[Any] = None
    unicode: Optional[Any] = None
    glyph_name: Optional[Any] = None
    d: Optional[Any] = None
    vert_text_orient: Optional[Any] = None
    arabic: Optional[Any] = None
    han: Optional[Any] = None
    horiz_adv_x: Optional[Any] = None
    vert_adv_y: Optional[Any] = None


@dataclass
class MissingGlyph(Element, m.StdAttrs):
    element_name = "missing-glyph"
    class_: Optional[Any] = None
    style: Optional[Any] = None
    d: Optional[Any] = None
    horiz_adv_x: Optional[Any] = None
    vert_adv_y: Optional[Any] = None


@dataclass
class HKern(Element, m.StdAttrs):
    element_name = "hkern"
    u1: Optional[Any] = None
    g1: Optional[Any] = None
    u2: Optional[Any] = None
    g2: Optional[Any] = None
    k: Optional[Any] = None


@dataclass
class VKern(Element, m.StdAttrs):
    element_name = "vkern"
    u1: Optional[Any] = None
    g1: Optional[Any] = None
    u2: Optional[Any] = None
    g2: Optional[Any] = None
    k: Optional[Any] = None


@dataclass
class FontFace(Element, m.StdAttrs):
    element_name = "font-face"
    font_family: Optional[Any] = None
    font_style: Optional[Any] = None
    font_variant: Optional[Any] = None
    font_weight: Optional[Any] = None
    font_stretch: Optional[Any] = None
    font_size: Optional[Any] = None
    unicode_range: Optional[Any] = None
    units_per_em: Optional[Any] = None
    panose_1: Optional[Any] = None
    stemv: Optional[Any] = None
    stemh: Optional[Any] = None
    slope: Optional[Any] = None
    cap_height: Optional[Any] = None
    x_height: Optional[Any] = None
    accent_height: Optional[Any] = None
    ascent: Optional[Any] = None
    descent: Optional[Any] = None
    widths: Optional[Any] = None
    bbox: Optional[Any] = None
    ideographic: Optional[Any] = None
    baseline: Optional[Any] = None
    centerline: Optional[Any] = None
    mathline: Optional[Any] = None
    hanging: Optional[Any] = None
    topline: Optional[Any] = None
    underline_position: Optional[Any] = None
    underline_thickness: Optional[Any] = None
    strikethrough_position: Optional[Any] = None
    strikethrough_thickness: Optional[Any] = None
    overline_position: Optional[Any] = None
    overline_thickness: Optional[Any] = None


@dataclass
class FontFaceSrc(Element, m.StdAttrs):
    element_name = "font-face-src"
    pass


@dataclass
class FontFaceURI(Element, m.StdAttrs):
    element_name = "font-face-uri"
    pass


@dataclass
class FontFaceFormat(Element, m.StdAttrs):
    element_name = "font-face-format"
    string: Optional[Any] = None


@dataclass
class FontFaceName(Element, m.StdAttrs):
    element_name = "font-face-name"
    name: Optional[Any] = None


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
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None
    x: Optional[Any] = None
    y: Optional[Any] = None
    width: Optional[Any] = None
    height: Optional[Any] = None
    content: Optional[Any] = None
