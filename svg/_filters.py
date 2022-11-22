from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Optional, Tuple

from . import _mixins as m
from ._transforms import Transform
from ._types import Length, Number, PreserveAspectRatio
from .elements import Element

if TYPE_CHECKING:
    from typing_extensions import Literal


@dataclass
class Filter(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/filter
    """
    element_name = "filter"
    externalResourcesRequired: Optional[bool] = None
    filterUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    primitiveUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    class_: Optional[list[str]] = None


@dataclass
class FeDistantLight(Element):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDistantLight
    """
    element_name = "feDistantLight"
    azimuth: Optional[Number] = None
    elevation: Optional[Number] = None


@dataclass
class FePointLight(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/fePointLight
    """
    element_name = "fePointLight"
    x: Length | Number | None = None
    y: Length | Number | None = None
    z: Length | Number | None = None


@dataclass
class FeSpotLight(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feSpotLight
    """
    element_name = "feSpotLight"
    x: Length | Number | None = None
    y: Length | Number | None = None
    z: Length | Number | None = None
    pointsAtX: Optional[Number] = None
    pointsAtY: Optional[Number] = None
    pointsAtZ: Optional[Number] = None
    specularExponent: Optional[Number] = None
    limitingConeAngle: Optional[Number] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None


@dataclass
class FeBlend(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feBlend
    """
    element_name = "feBlend"
    in2: Optional[str] = None
    mode: Optional[Literal[
        "normal", "multiply", "screen", "overlay", "darken", "lighten", "color-dodge",
        "color-burn", "hard-light", "soft-light", "difference", "exclusion", "hue",
        "saturation", "color", "luminosity", "inherit",
    ]] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeColorMatrix(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feColorMatrix
    """
    element_name = "feColorMatrix"
    type: Optional[Literal["matrix", "saturate", "hueRotate", "luminanceToAlpha"]] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    values: Optional[str] = None


@dataclass
class FeComponentTransfer(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feComponentTransfer
    """
    element_name = "feComponentTransfer"
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeFuncR(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncR
    """
    element_name = "feFuncR"
    type2: Optional[Literal["identity", "table", "discrete", "linear", "gamma"]] = None


@dataclass
class FeFuncG(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncG
    """
    element_name = "feFuncG"
    type2: Optional[Literal["identity", "table", "discrete", "linear", "gamma"]] = None


@dataclass
class FeFuncB(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncB
    """
    element_name = "feFuncB"
    type2: Optional[Literal["identity", "table", "discrete", "linear", "gamma"]] = None


@dataclass
class FeFuncA(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncA
    """
    element_name = "feFuncA"
    type3: Optional[Literal["identity", "table", "discrete", "linear", "gamma"]] = None


@dataclass
class FeComposite(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feComposite
    """
    element_name = "feComposite"
    in2: Optional[str] = None
    operator: Optional[Literal["over", "in", "out", "atop", "xor", "lighter", "arithmetic"]] = None
    k1: Optional[Number] = None
    k2: Optional[Number] = None
    k3: Optional[Number] = None
    k4: Optional[Number] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeConvolveMatrix(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feConvolveMatrix
    """
    element_name = "feConvolveMatrix"
    order: Optional[Any] = None
    kernelMatrix: Optional[str] = None
    divisor: Optional[Any] = None
    bias: Optional[Any] = None
    targetX: Optional[Any] = None
    targetY: Optional[Any] = None
    edgeMode: Optional[Literal["duplicate", "wrap", "none"]] = None
    preserveAlpha: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeDiffuseLighting(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDiffuseLighting
    """
    element_name = "feDiffuseLighting"
    surfaceScale: Optional[Number] = None
    diffuseConstant: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    lighting_color: Optional[str] = None


@dataclass
class FeDisplacementMap(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDisplacementMap
    """
    element_name = "feDisplacementMap"
    in2: Optional[str] = None
    scale: Optional[Any] = None
    xChannelSelector: Optional[Any] = None
    yChannelSelector: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeFlood(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFlood
    """
    element_name = "feFlood"
    flood_opacity: Optional[Number] = None
    flood_color: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeGaussianBlur(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feGaussianBlur
    """
    element_name = "feGaussianBlur"
    stdDeviation: Optional[Tuple[Number, Number]] = None
    edgeMode: Optional[Literal["duplicate", "wrap", "none"]] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeImage(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feImage
    """
    element_name = "feImage"
    externalResourcesRequired: Optional[Any] = None
    transform: Optional[list[Transform]] = None
    preserveAspectRatio: Optional[PreserveAspectRatio] = None
    href: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeMerge(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feMerge
    """
    element_name = "feMerge"
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeMergeNode(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feMergeNode
    """
    element_name = "feMergeNode"
    in_: Optional[str] = None


@dataclass
class FeMorphology(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feMorphology
    """
    element_name = "feMorphology"
    operator: Optional[Literal["erode", "dilate"]] = None
    radius: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeDropShadow(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDropShadow
    """
    element_name = "feDropShadow"
    dx: Optional[Any] = None
    dy: Optional[Any] = None
    flood_opacity: Optional[Number] = None
    flood_color: Optional[str] = None
    stdDeviation: Optional[Tuple[Number, Number]] = None
    class_: Optional[list[str]] = None


@dataclass
class FeOffset(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feOffset
    """
    element_name = "feOffset"
    dx: Optional[Any] = None
    dy: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeSpecularLighting(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feSpecularLighting
    """
    element_name = "feSpecularLighting"
    surfaceScale: Optional[Number] = None
    specularConstant: Optional[Number] = None
    specularExponent: Optional[Number] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    lighting_color: Optional[str] = None


@dataclass
class FeTile(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTile
    """
    element_name = "feTile"
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeTurbulence(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTurbulence
    """
    element_name = "feTurbulence"
    baseFrequency: Optional[str] = None
    numOctaves: Optional[int] = None
    seed: Optional[Number] = None
    stitchTiles: Optional[Literal["noStitch", "stitch"]] = None
    type: Optional[Literal["fractalNoise", "turbulence"]] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[list[str]] = None
    width: Length | Number | None = None
    height: Length | Number | None = None
