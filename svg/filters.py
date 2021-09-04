from dataclasses import dataclass
from typing import Any, List, Optional, Union

from typing_extensions import Literal

from . import _mixins as m, elements as e, values
from .elements import Element
from .transforms import Transform


@dataclass
class Filter(Element, m.FilterPrimitive):
    element_name = "filter"
    elements: Optional[List[Union[
        "FeBlend",
        "FeFlood",
        "FeColorMatrix",
        "FeComponentTransfer",
        "FeComposite",
        "FeConvolveMatrix",
        "FeDiffuseLighting",
        "FeDisplacementMap",
        "FeGaussianBlur",
        "FeImage",
        "FeMerge",
        "FeMorphology",
        "FeOffset",
        "FeSpecularLighting",
        "FeTile",
        "FeTurbulence",
        e.Animate,
        e.Set,
    ]]] = None
    externalResourcesRequired: Optional[bool] = None
    filterUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    primitiveUnits: Optional[Literal["userSpaceOnUse", "objectBoundingBox"]] = None
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
    class_: Optional[values.Classes] = None


@dataclass
class FeDistantLight(Element):
    element_name = "feDistantLight"
    azimuth: Optional[values.Number] = None
    elevation: Optional[values.Number] = None


@dataclass
class FePointLight(Element, m.FilterPrimitive):
    element_name = "fePointLight"
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    z: Union[values.Length, values.Number, None] = None


@dataclass
class FeSpotLight(Element, m.FilterPrimitive):
    element_name = "feSpotLight"
    x: Union[values.Length, values.Number, None] = None
    y: Union[values.Length, values.Number, None] = None
    z: Union[values.Length, values.Number, None] = None
    pointsAtX: Optional[values.Number] = None
    pointsAtY: Optional[values.Number] = None
    pointsAtZ: Optional[values.Number] = None
    specularExponent: Optional[values.Number] = None
    limitingConeAngle: Optional[values.Number] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None


@dataclass
class FeBlend(Element, m.FilterPrimitive):
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
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeColorMatrix(Element, m.FilterPrimitive):
    element_name = "feColorMatrix"
    type: Optional[Literal["matrix", "saturate", "hueRotate", "luminanceToAlpha"]] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
    values: Optional[str] = None


@dataclass
class FeComponentTransfer(Element, m.FilterPrimitive):
    element_name = "feComponentTransfer"
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeFuncR(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    element_name = "feFuncR"
    type2: Optional[Literal["identity", "table", "discrete", "linear", "gamma"]] = None


@dataclass
class FeFuncG(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    element_name = "feFuncG"
    type2: Optional[Literal["identity", "table", "discrete", "linear", "gamma"]] = None


@dataclass
class FeFuncB(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    element_name = "feFuncB"
    type2: Optional[Literal["identity", "table", "discrete", "linear", "gamma"]] = None


@dataclass
class FeFuncA(Element, m.FilterPrimitive, m.ComponentTransferFunction):
    element_name = "feFuncA"
    type3: Optional[Literal["identity", "table", "discrete", "linear", "gamma"]] = None


@dataclass
class FeComposite(Element, m.FilterPrimitive):
    element_name = "feComposite"
    in2: Optional[str] = None
    operator: Optional[Literal["over", "in", "out", "atop", "xor", "lighter", "arithmetic"]] = None
    k1: Optional[values.Number] = None
    k2: Optional[values.Number] = None
    k3: Optional[values.Number] = None
    k4: Optional[values.Number] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeConvolveMatrix(Element, m.FilterPrimitive):
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
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeDiffuseLighting(Element, m.FilterPrimitive):
    element_name = "feDiffuseLighting"
    elements: Optional[List[Union[e.Animate, e.Set]]] = None
    surfaceScale: Optional[values.Number] = None
    diffuseConstant: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
    lighting_color: Optional[str] = None


@dataclass
class FeDisplacementMap(Element, m.FilterPrimitive):
    element_name = "feDisplacementMap"
    in2: Optional[str] = None
    scale: Optional[Any] = None
    xChannelSelector: Optional[Any] = None
    yChannelSelector: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeFlood(Element, m.FilterPrimitive):
    element_name = "feFlood"
    flood_opacity: Optional[values.Opacity] = None
    flood_color: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeGaussianBlur(Element, m.FilterPrimitive):
    element_name = "feGaussianBlur"
    stdDeviation: Optional[values.NumberOptionalNumber] = None
    edgeMode: Optional[Literal["duplicate", "wrap", "none"]] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeImage(Element, m.FilterPrimitive):
    element_name = "feImage"
    externalResourcesRequired: Optional[Any] = None
    transform: Optional[List[Transform]] = None
    preserveAspectRatio: Optional[values.PreserveAspectRatio] = None
    href: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeMerge(Element, m.FilterPrimitive):
    element_name = "feMerge"
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeMergeNode(Element, m.FilterPrimitive):
    element_name = "feMergeNode"
    in_: Optional[str] = None


@dataclass
class FeMorphology(Element, m.FilterPrimitive):
    element_name = "feMorphology"
    operator: Optional[Literal["erode", "dilate"]] = None
    radius: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeOffset(Element, m.FilterPrimitive):
    element_name = "feOffset"
    dx: Optional[Any] = None
    dy: Optional[Any] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeSpecularLighting(Element, m.FilterPrimitive):
    element_name = "feSpecularLighting"
    elements: Optional[List[Union[e.Animate, e.Set]]] = None
    surfaceScale: Optional[values.Number] = None
    specularConstant: Optional[values.Number] = None
    specularExponent: Optional[values.Number] = None
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
    lighting_color: Optional[str] = None


@dataclass
class FeTile(Element, m.FilterPrimitive):
    element_name = "feTile"
    in_: Optional[str] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None


@dataclass
class FeTurbulence(Element, m.FilterPrimitive):
    element_name = "feTurbulence"
    baseFrequency: Optional[str] = None
    numOctaves: Optional[int] = None
    seed: Optional[values.Number] = None
    stitchTiles: Optional[Literal["noStitch", "stitch"]] = None
    type: Optional[Literal["fractalNoise", "turbulence"]] = None
    color_interpolation_filters: Optional[Literal["auto", "sRGB", "linearRGB", "inherit"]] = None
    result: Optional[str] = None
    class_: Optional[values.Classes] = None
    width: Union[values.Length, values.Number, None] = None
    height: Union[values.Length, values.Number, None] = None
