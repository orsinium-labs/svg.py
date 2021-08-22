from dataclasses import dataclass, asdict
from enum import Enum
from typing import Any, Dict, List, Optional
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
class Symbol(Element, m.StdAttrs):
    element_name = "symbol"
    pass


@dataclass
class Use(Element, m.StdAttrs):
    element_name = "use"
    pass


@dataclass
class Image(Element, m.StdAttrs):
    element_name = "image"
    pass


@dataclass
class Switch(Element, m.StdAttrs):
    element_name = "switch"
    pass


@dataclass
class Style(Element, m.StdAttrs):
    element_name = "style"
    pass


@dataclass
class Path(Element, m.StdAttrs):
    element_name = "path"
    pass


@dataclass
class Rect(Element, m.StdAttrs):
    element_name = "rect"
    pass


@dataclass
class Circle(Element, m.StdAttrs):
    element_name = "circle"
    pass


@dataclass
class Ellipse(Element, m.StdAttrs):
    element_name = "ellipse"
    pass


@dataclass
class Line(Element, m.StdAttrs):
    element_name = "line"
    pass


@dataclass
class Polyline(Element, m.StdAttrs):
    element_name = "polyline"
    pass


@dataclass
class Polygon(Element, m.StdAttrs):
    element_name = "polygon"
    pass


@dataclass
class Text(Element, m.StdAttrs):
    element_name = "text"
    pass


@dataclass
class Tspan(Element, m.StdAttrs):
    element_name = "tspan"
    pass


@dataclass
class Tref(Element, m.StdAttrs):
    element_name = "tref"
    pass


@dataclass
class TextPath(Element, m.StdAttrs):
    element_name = "textPath"
    pass


@dataclass
class AltGlyph(Element, m.StdAttrs):
    element_name = "altGlyph"
    pass


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
    pass


@dataclass
class Marker(Element, m.StdAttrs):
    element_name = "marker"
    pass


@dataclass
class ColorProfile(Element, m.StdAttrs):
    element_name = "color-profile"
    pass


@dataclass
class LinearGradient(Element, m.StdAttrs):
    element_name = "linearGradient"
    pass


@dataclass
class RadialGradient(Element, m.StdAttrs):
    element_name = "radialGradient"
    pass


@dataclass
class Stop(Element, m.StdAttrs):
    element_name = "stop"
    pass


@dataclass
class Pattern(Element, m.StdAttrs):
    element_name = "pattern"
    pass


@dataclass
class ClipPath(Element, m.StdAttrs):
    element_name = "clipPath"
    pass


@dataclass
class Mask(Element, m.StdAttrs):
    element_name = "mask"
    pass


@dataclass
class Filter(Element, m.StdAttrs):
    element_name = "filter"
    pass


@dataclass
class FeDistantLight(Element, m.StdAttrs):
    element_name = "feDistantLight"
    pass


@dataclass
class FePointLight(Element, m.StdAttrs):
    element_name = "fePointLight"
    pass


@dataclass
class FeSpotLight(Element, m.StdAttrs):
    element_name = "feSpotLight"
    pass


@dataclass
class FeBlend(Element, m.StdAttrs):
    element_name = "feBlend"
    pass


@dataclass
class FeColorMatrix(Element, m.StdAttrs):
    element_name = "feColorMatrix"
    pass


@dataclass
class FeComponentTransfer(Element, m.StdAttrs):
    element_name = "feComponentTransfer"
    pass


@dataclass
class FeFuncR(Element, m.StdAttrs):
    element_name = "feFuncR"
    pass


@dataclass
class FeFuncG(Element, m.StdAttrs):
    element_name = "feFuncG"
    pass


@dataclass
class FeFuncB(Element, m.StdAttrs):
    element_name = "feFuncB"
    pass


@dataclass
class FeFuncA(Element, m.StdAttrs):
    element_name = "feFuncA"
    pass


@dataclass
class FeComposite(Element, m.StdAttrs):
    element_name = "feComposite"
    pass


@dataclass
class FeConvolveMatrix(Element, m.StdAttrs):
    element_name = "feConvolveMatrix"
    pass


@dataclass
class FeDiffuseLighting(Element, m.StdAttrs):
    element_name = "feDiffuseLighting"
    pass


@dataclass
class FeDisplacementMap(Element, m.StdAttrs):
    element_name = "feDisplacementMap"
    pass


@dataclass
class FeFlood(Element, m.StdAttrs):
    element_name = "feFlood"
    pass


@dataclass
class FeGaussianBlur(Element, m.StdAttrs):
    element_name = "feGaussianBlur"
    pass


@dataclass
class FeImage(Element, m.StdAttrs):
    element_name = "feImage"
    pass


@dataclass
class FeMerge(Element, m.StdAttrs):
    element_name = "feMerge"
    pass


@dataclass
class FeMergeNode(Element, m.StdAttrs):
    element_name = "feMergeNode"
    pass


@dataclass
class FeMorphology(Element, m.StdAttrs):
    element_name = "feMorphology"
    pass


@dataclass
class FeOffset(Element, m.StdAttrs):
    element_name = "feOffset"
    pass


@dataclass
class FeSpecularLighting(Element, m.StdAttrs):
    element_name = "feSpecularLighting"
    pass


@dataclass
class FeTile(Element, m.StdAttrs):
    element_name = "feTile"
    pass


@dataclass
class FeTurbulence(Element, m.StdAttrs):
    element_name = "feTurbulence"
    pass


@dataclass
class Cursor(Element, m.StdAttrs):
    element_name = "cursor"
    pass


@dataclass
class A(Element, m.StdAttrs):
    element_name = "a"
    pass


@dataclass
class View(Element, m.StdAttrs):
    element_name = "view"
    pass


@dataclass
class Script(Element, m.StdAttrs):
    element_name = "script"
    pass


@dataclass
class Animate(Element, m.StdAttrs):
    element_name = "animate"
    pass


@dataclass
class Set(Element, m.StdAttrs):
    element_name = "set"
    pass


@dataclass
class AnimateMotion(Element, m.StdAttrs):
    element_name = "animateMotion"
    pass


@dataclass
class MPath(Element, m.StdAttrs):
    element_name = "mpath"
    pass


@dataclass
class AnimateColor(Element, m.StdAttrs):
    element_name = "animateColor"
    pass


@dataclass
class AnimateTransform(Element, m.StdAttrs):
    element_name = "animateTransform"
    pass


@dataclass
class Font(Element, m.StdAttrs):
    element_name = "font"
    pass


@dataclass
class Glyph(Element, m.StdAttrs):
    element_name = "glyph"
    pass


@dataclass
class MissingGlyph(Element, m.StdAttrs):
    element_name = "missing-glyph"
    pass


@dataclass
class HKern(Element, m.StdAttrs):
    element_name = "hkern"
    pass


@dataclass
class VKern(Element, m.StdAttrs):
    element_name = "vkern"
    pass


@dataclass
class FontFace(Element, m.StdAttrs):
    element_name = "font-face"
    pass


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
    pass


@dataclass
class FontFaceName(Element, m.StdAttrs):
    element_name = "font-face-name"
    pass


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
    pass
