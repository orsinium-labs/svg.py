from dataclasses import dataclass
from typing import Any, Optional
from . import _mixins as m, values
from .elements import Element


@dataclass
class Filter(Element, m.StdAttrs):
    element_name = "filter"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    filterUnits: Optional[Any] = None
    primitiveUnits: Optional[Any] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    filterRes: Optional[Any] = None


@dataclass
class FeDistantLight(Element, m.StdAttrs):
    element_name = "feDistantLight"
    azimuth: Optional[Any] = None
    elevation: Optional[Any] = None


@dataclass
class FePointLight(Element, m.StdAttrs):
    element_name = "fePointLight"
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    z: Optional[Any] = None


@dataclass
class FeSpotLight(Element, m.StdAttrs):
    element_name = "feSpotLight"
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    z: Optional[Any] = None
    pointsAtX: Optional[Any] = None
    pointsAtY: Optional[Any] = None
    pointsAtZ: Optional[Any] = None
    specularExponent: Optional[Any] = None
    limitingConeAngle: Optional[Any] = None


@dataclass
class FeBlend(Element, m.StdAttrs):
    element_name = "feBlend"
    in2: Optional[Any] = None
    mode: Optional[Any] = None


@dataclass
class FeColorMatrix(Element, m.StdAttrs):
    element_name = "feColorMatrix"
    type: Optional[Any] = None
    values: Optional[Any] = None


@dataclass
class FeComponentTransfer(Element, m.StdAttrs):
    element_name = "feComponentTransfer"
    pass


@dataclass
class FeFuncR(Element, m.StdAttrs):
    element_name = "feFuncR"
    type2: Optional[Any] = None


@dataclass
class FeFuncG(Element, m.StdAttrs):
    element_name = "feFuncG"
    type2: Optional[Any] = None


@dataclass
class FeFuncB(Element, m.StdAttrs):
    element_name = "feFuncB"
    type2: Optional[Any] = None


@dataclass
class FeFuncA(Element, m.StdAttrs):
    element_name = "feFuncA"
    type3: Optional[Any] = None


@dataclass
class FeComposite(Element, m.StdAttrs):
    element_name = "feComposite"
    in2: Optional[Any] = None
    operator: Optional[Any] = None
    k1: Optional[Any] = None
    k2: Optional[Any] = None
    k3: Optional[Any] = None
    k4: Optional[Any] = None


@dataclass
class FeConvolveMatrix(Element, m.StdAttrs):
    element_name = "feConvolveMatrix"
    order: Optional[Any] = None
    kernelMatrix: Optional[Any] = None
    divisor: Optional[Any] = None
    bias: Optional[Any] = None
    targetX: Optional[Any] = None
    targetY: Optional[Any] = None
    edgeMode: Optional[Any] = None
    kernelUnitLength: Optional[Any] = None
    preserveAlpha: Optional[Any] = None


@dataclass
class FeDiffuseLighting(Element, m.StdAttrs):
    element_name = "feDiffuseLighting"
    class_: Optional[Any] = None
    style: Optional[Any] = None
    surfaceScale: Optional[Any] = None
    diffuseConstant: Optional[Any] = None


@dataclass
class FeDisplacementMap(Element, m.StdAttrs):
    element_name = "feDisplacementMap"
    in2: Optional[Any] = None
    scale: Optional[Any] = None
    xChannelSelector: Optional[Any] = None
    yChannelSelector: Optional[Any] = None


@dataclass
class FeFlood(Element, m.StdAttrs):
    element_name = "feFlood"
    class_: Optional[Any] = None
    style: Optional[Any] = None


@dataclass
class FeGaussianBlur(Element, m.StdAttrs):
    element_name = "feGaussianBlur"
    stdDeviation: Optional[Any] = None


@dataclass
class FeImage(Element, m.StdAttrs):
    element_name = "feImage"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None


@dataclass
class FeMerge(Element, m.StdAttrs):
    element_name = "feMerge"
    pass


@dataclass
class FeMergeNode(Element, m.StdAttrs):
    element_name = "feMergeNode"
    in_: Optional[Any] = None


@dataclass
class FeMorphology(Element, m.StdAttrs):
    element_name = "feMorphology"
    operator: Optional[Any] = None
    radius: Optional[Any] = None


@dataclass
class FeOffset(Element, m.StdAttrs):
    element_name = "feOffset"
    dx: Optional[Any] = None
    dy: Optional[Any] = None


@dataclass
class FeSpecularLighting(Element, m.StdAttrs):
    element_name = "feSpecularLighting"
    class_: Optional[Any] = None
    style: Optional[Any] = None
    surfaceScale: Optional[Any] = None
    specularConstant: Optional[Any] = None
    specularExponent: Optional[Any] = None


@dataclass
class FeTile(Element, m.StdAttrs):
    element_name = "feTile"
    pass


@dataclass
class FeTurbulence(Element, m.StdAttrs):
    element_name = "feTurbulence"
    baseFrequency: Optional[Any] = None
    numOctaves: Optional[Any] = None
    seed: Optional[Any] = None
    stitchTiles: Optional[Any] = None
    type: Optional[Any] = None
