from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

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
    externalResourcesRequired: bool | None = None
    filterUnits: Literal["userSpaceOnUse", "objectBoundingBox"] | None = None
    primitiveUnits: Literal["userSpaceOnUse", "objectBoundingBox"] | None = None
    x: Length | Number | None = None
    y: Length | Number | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    class_: list[str] | None = None


@dataclass
class FeDistantLight(Element):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDistantLight
    """
    element_name = "feDistantLight"
    azimuth: Number | None = None
    elevation: Number | None = None


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
    pointsAtX: Number | None = None
    pointsAtY: Number | None = None
    pointsAtZ: Number | None = None
    specularExponent: Number | None = None
    limitingConeAngle: Number | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None


@dataclass
class FeBlend(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feBlend
    """
    element_name = "feBlend"
    in2: str | None = None
    mode: None | Literal[
        "normal", "multiply", "screen", "overlay", "darken", "lighten", "color-dodge",
        "color-burn", "hard-light", "soft-light", "difference", "exclusion", "hue",
        "saturation", "color", "luminosity", "inherit",
    ] = None
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeColorMatrix(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feColorMatrix
    """
    element_name = "feColorMatrix"
    type: Literal["matrix", "saturate", "hueRotate", "luminanceToAlpha"] | None = None
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    values: str | None = None


@dataclass
class FeComponentTransfer(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feComponentTransfer
    """
    element_name = "feComponentTransfer"
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeFuncR(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncR
    """
    element_name = "feFuncR"
    type2: Literal["identity", "table", "discrete", "linear", "gamma"] | None = None


@dataclass
class FeFuncG(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncG
    """
    element_name = "feFuncG"
    type2: Literal["identity", "table", "discrete", "linear", "gamma"] | None = None


@dataclass
class FeFuncB(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncB
    """
    element_name = "feFuncB"
    type2: Literal["identity", "table", "discrete", "linear", "gamma"] | None = None


@dataclass
class FeFuncA(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncA
    """
    element_name = "feFuncA"
    type3: Literal["identity", "table", "discrete", "linear", "gamma"] | None = None


@dataclass
class FeComposite(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feComposite
    """
    element_name = "feComposite"
    in2: str | None = None
    operator: Literal["over", "in", "out", "atop", "xor", "lighter", "arithmetic"] | None = None
    k1: Number | None = None
    k2: Number | None = None
    k3: Number | None = None
    k4: Number | None = None
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeConvolveMatrix(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feConvolveMatrix
    """
    element_name = "feConvolveMatrix"
    order: Any | None = None
    kernelMatrix: str | None = None
    divisor: Any | None = None
    bias: Any | None = None
    targetX: Any | None = None
    targetY: Any | None = None
    edgeMode: Literal["duplicate", "wrap", "none"] | None = None
    preserveAlpha: Any | None = None
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeDiffuseLighting(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDiffuseLighting
    """
    element_name = "feDiffuseLighting"
    surfaceScale: Number | None = None
    diffuseConstant: Any | None = None
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    lighting_color: str | None = None


@dataclass
class FeDisplacementMap(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDisplacementMap
    """
    element_name = "feDisplacementMap"
    in2: str | None = None
    scale: Any | None = None
    xChannelSelector: Any | None = None
    yChannelSelector: Any | None = None
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeFlood(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFlood
    """
    element_name = "feFlood"
    flood_opacity: Number | None = None
    flood_color: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeGaussianBlur(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feGaussianBlur
    """
    element_name = "feGaussianBlur"
    stdDeviation: Number | tuple[Number, Number] | None = None
    edgeMode: Literal["duplicate", "wrap", "none"] | None = None
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeImage(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feImage
    """
    element_name = "feImage"
    externalResourcesRequired: Any | None = None
    transform: list[Transform] | None = None
    preserveAspectRatio: PreserveAspectRatio | None = None
    href: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeMerge(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feMerge
    """
    element_name = "feMerge"
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeMergeNode(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feMergeNode
    """
    element_name = "feMergeNode"
    in_: str | None = None


@dataclass
class FeMorphology(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feMorphology
    """
    element_name = "feMorphology"
    operator: Literal["erode", "dilate"] | None = None
    radius: Any | None = None
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeDropShadow(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDropShadow
    """
    element_name = "feDropShadow"
    dx: Any | None = None
    dy: Any | None = None
    flood_opacity: Number | None = None
    flood_color: str | None = None
    stdDeviation: Number | tuple[Number, Number] | None = None
    class_: list[str] | None = None


@dataclass
class FeOffset(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feOffset
    """
    element_name = "feOffset"
    dx: Any | None = None
    dy: Any | None = None
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeSpecularLighting(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feSpecularLighting
    """
    element_name = "feSpecularLighting"
    surfaceScale: Number | None = None
    specularConstant: Number | None = None
    specularExponent: Number | None = None
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
    lighting_color: str | None = None


@dataclass
class FeTile(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTile
    """
    element_name = "feTile"
    in_: str | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None


@dataclass
class FeTurbulence(Element, m.FilterPrimitive):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTurbulence
    """
    element_name = "feTurbulence"
    baseFrequency: str | None = None
    numOctaves: int | None = None
    seed: Number | None = None
    stitchTiles: Literal["noStitch", "stitch"] | None = None
    type: Literal["fractalNoise", "turbulence"] | None = None
    color_interpolation_filters: Literal["auto", "sRGB", "linearRGB", "inherit"] | None = None
    result: str | None = None
    class_: list[str] | None = None
    width: Length | Number | None = None
    height: Length | Number | None = None
