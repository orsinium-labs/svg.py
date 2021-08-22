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
            content = ''.join(str(e) for e in elements)
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
class G(Element):
    element_name = "g"
    pass


@dataclass
class Defs(Element):
    element_name = "defs"
    pass


@dataclass
class Desc(Element):
    element_name = "desc"
    pass


@dataclass
class Title(Element):
    element_name = "title"
    pass


@dataclass
class Symbol(Element):
    element_name = "symbol"
    pass


@dataclass
class Use(Element):
    element_name = "use"
    pass


@dataclass
class Image(Element):
    element_name = "image"
    pass


@dataclass
class Switch(Element):
    element_name = "switch"
    pass


@dataclass
class Style(Element):
    element_name = "style"
    pass


@dataclass
class Path(Element):
    element_name = "path"
    pass


@dataclass
class Rect(Element):
    element_name = "rect"
    pass


@dataclass
class Circle(Element):
    element_name = "circle"
    pass


@dataclass
class Ellipse(Element):
    element_name = "ellipse"
    pass


@dataclass
class Line(Element):
    element_name = "line"
    pass


@dataclass
class Polyline(Element):
    element_name = "polyline"
    pass


@dataclass
class Polygon(Element):
    element_name = "polygon"
    pass


@dataclass
class Text(Element):
    element_name = "text"
    pass


@dataclass
class Tspan(Element):
    element_name = "tspan"
    pass


@dataclass
class Tref(Element):
    element_name = "tref"
    pass


@dataclass
class TextPath(Element):
    element_name = "textPath"
    pass


@dataclass
class AltGlyph(Element):
    element_name = "altGlyph"
    pass


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
    pass


@dataclass
class Marker(Element):
    element_name = "marker"
    pass


@dataclass
class ColorProfile(Element):
    element_name = "color-profile"
    pass


@dataclass
class LinearGradient(Element):
    element_name = "linearGradient"
    pass


@dataclass
class RadialGradient(Element):
    element_name = "radialGradient"
    pass


@dataclass
class Stop(Element):
    element_name = "stop"
    pass


@dataclass
class Pattern(Element):
    element_name = "pattern"
    pass


@dataclass
class ClipPath(Element):
    element_name = "clipPath"
    pass


@dataclass
class Mask(Element):
    element_name = "mask"
    pass


@dataclass
class Filter(Element):
    element_name = "filter"
    pass


@dataclass
class FeDistantLight(Element):
    element_name = "feDistantLight"
    pass


@dataclass
class FePointLight(Element):
    element_name = "fePointLight"
    pass


@dataclass
class FeSpotLight(Element):
    element_name = "feSpotLight"
    pass


@dataclass
class FeBlend(Element):
    element_name = "feBlend"
    pass


@dataclass
class FeColorMatrix(Element):
    element_name = "feColorMatrix"
    pass


@dataclass
class FeComponentTransfer(Element):
    element_name = "feComponentTransfer"
    pass


@dataclass
class FeFuncR(Element):
    element_name = "feFuncR"
    pass


@dataclass
class FeFuncG(Element):
    element_name = "feFuncG"
    pass


@dataclass
class FeFuncB(Element):
    element_name = "feFuncB"
    pass


@dataclass
class FeFuncA(Element):
    element_name = "feFuncA"
    pass


@dataclass
class FeComposite(Element):
    element_name = "feComposite"
    pass


@dataclass
class FeConvolveMatrix(Element):
    element_name = "feConvolveMatrix"
    pass


@dataclass
class FeDiffuseLighting(Element):
    element_name = "feDiffuseLighting"
    pass


@dataclass
class FeDisplacementMap(Element):
    element_name = "feDisplacementMap"
    pass


@dataclass
class FeFlood(Element):
    element_name = "feFlood"
    pass


@dataclass
class FeGaussianBlur(Element):
    element_name = "feGaussianBlur"
    pass


@dataclass
class FeImage(Element):
    element_name = "feImage"
    pass


@dataclass
class FeMerge(Element):
    element_name = "feMerge"
    pass


@dataclass
class FeMergeNode(Element):
    element_name = "feMergeNode"
    pass


@dataclass
class FeMorphology(Element):
    element_name = "feMorphology"
    pass


@dataclass
class FeOffset(Element):
    element_name = "feOffset"
    pass


@dataclass
class FeSpecularLighting(Element):
    element_name = "feSpecularLighting"
    pass


@dataclass
class FeTile(Element):
    element_name = "feTile"
    pass


@dataclass
class FeTurbulence(Element):
    element_name = "feTurbulence"
    pass


@dataclass
class Cursor(Element):
    element_name = "cursor"
    pass


@dataclass
class A(Element):
    element_name = "a"
    pass


@dataclass
class View(Element):
    element_name = "view"
    pass


@dataclass
class Script(Element):
    element_name = "script"
    pass


@dataclass
class Animate(Element):
    element_name = "animate"
    pass


@dataclass
class Set(Element):
    element_name = "set"
    pass


@dataclass
class AnimateMotion(Element):
    element_name = "animateMotion"
    pass


@dataclass
class MPath(Element):
    element_name = "mpath"
    pass


@dataclass
class AnimateColor(Element):
    element_name = "animateColor"
    pass


@dataclass
class AnimateTransform(Element):
    element_name = "animateTransform"
    pass


@dataclass
class Font(Element):
    element_name = "font"
    pass


@dataclass
class Glyph(Element):
    element_name = "glyph"
    pass


@dataclass
class MissingGlyph(Element):
    element_name = "missing-glyph"
    pass


@dataclass
class HKern(Element):
    element_name = "hkern"
    pass


@dataclass
class VKern(Element):
    element_name = "vkern"
    pass


@dataclass
class FontFace(Element):
    element_name = "font-face"
    pass


@dataclass
class FontFaceSrc(Element):
    element_name = "font-face-src"
    pass


@dataclass
class FontFaceURI(Element):
    element_name = "font-face-uri"
    pass


@dataclass
class FontFaceFormat(Element):
    element_name = "font-face-format"
    pass


@dataclass
class FontFaceName(Element):
    element_name = "font-face-name"
    pass


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
    pass
