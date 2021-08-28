from dataclasses import dataclass
from typing import Any, List, Optional, Union
from . import values, elements as e
from .elements import Element


@dataclass
class Filter(Element):
    element_name = "filter"
    elements: Optional[List[Union[
        'FeBlend', 'FeFlood', 'FeColorMatrix', 'FeComponentTransfer', 'FeComposite',
        'FeConvolveMatrix', 'FeDiffuseLighting',
        'FeDisplacementMap', 'FeGaussianBlur', 'FeImage', 'FeMerge',
        'FeMorphology', 'FeOffset', 'FeSpecularLighting',
        'FeTile', 'FeTurbulence', e.Animate, e.Set,
    ]]] = None
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    filterUnits: Optional[Any] = None
    primitiveUnits: Optional[Any] = None
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    width: Optional[values.Length] = None
    height: Optional[values.Length] = None
    filterRes: Optional[str] = None


@dataclass
class FeDistantLight(Element):
    element_name = "feDistantLight"
    azimuth: Optional[Any] = None
    elevation: Optional[Any] = None


@dataclass
class FePointLight(Element):
    element_name = "fePointLight"
    x: Optional[values.Coordinate] = None
    y: Optional[values.Coordinate] = None
    z: Optional[Any] = None


@dataclass
class FeSpotLight(Element):
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
class FeBlend(Element):
    element_name = "feBlend"
    in2: Optional[str] = None
    mode: Optional[Any] = None


@dataclass
class FeColorMatrix(Element):
    element_name = "feColorMatrix"
    type: Optional[Any] = None
    values: Optional[str] = None


@dataclass
class FeComponentTransfer(Element):
    element_name = "feComponentTransfer"
    pass


@dataclass
class FeFuncR(Element):
    element_name = "feFuncR"
    type2: Optional[Any] = None


@dataclass
class FeFuncG(Element):
    element_name = "feFuncG"
    type2: Optional[Any] = None


@dataclass
class FeFuncB(Element):
    element_name = "feFuncB"
    type2: Optional[Any] = None


@dataclass
class FeFuncA(Element):
    element_name = "feFuncA"
    type3: Optional[Any] = None


@dataclass
class FeComposite(Element):
    element_name = "feComposite"
    in2: Optional[str] = None
    operator: Optional[Any] = None
    k1: Optional[Any] = None
    k2: Optional[Any] = None
    k3: Optional[Any] = None
    k4: Optional[Any] = None


@dataclass
class FeConvolveMatrix(Element):
    element_name = "feConvolveMatrix"
    order: Optional[Any] = None
    kernelMatrix: Optional[str] = None
    divisor: Optional[Any] = None
    bias: Optional[Any] = None
    targetX: Optional[Any] = None
    targetY: Optional[Any] = None
    edgeMode: Optional[Any] = None
    kernelUnitLength: Optional[str] = None
    preserveAlpha: Optional[Any] = None


@dataclass
class FeDiffuseLighting(Element):
    element_name = "feDiffuseLighting"
    elements: Optional[List[Union[e.Animate, e.Set, e.AnimateColor]]] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    surfaceScale: Optional[Any] = None
    diffuseConstant: Optional[Any] = None


@dataclass
class FeDisplacementMap(Element):
    element_name = "feDisplacementMap"
    in2: Optional[str] = None
    scale: Optional[Any] = None
    xChannelSelector: Optional[Any] = None
    yChannelSelector: Optional[Any] = None


@dataclass
class FeFlood(Element):
    element_name = "feFlood"
    class_: Optional[Any] = None
    style: Optional[Any] = None


@dataclass
class FeGaussianBlur(Element):
    element_name = "feGaussianBlur"
    stdDeviation: Optional[Any] = None


@dataclass
class FeImage(Element):
    element_name = "feImage"
    externalResourcesRequired: Optional[Any] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    transform: Optional[Any] = None


@dataclass
class FeMerge(Element):
    element_name = "feMerge"
    pass


@dataclass
class FeMergeNode(Element):
    element_name = "feMergeNode"
    in_: Optional[str] = None


@dataclass
class FeMorphology(Element):
    element_name = "feMorphology"
    operator: Optional[Any] = None
    radius: Optional[Any] = None


@dataclass
class FeOffset(Element):
    element_name = "feOffset"
    dx: Optional[Any] = None
    dy: Optional[Any] = None


@dataclass
class FeSpecularLighting(Element):
    element_name = "feSpecularLighting"
    elements: Optional[List[Union[e.Animate, e.Set, e.AnimateColor]]] = None
    class_: Optional[Any] = None
    style: Optional[Any] = None
    surfaceScale: Optional[Any] = None
    specularConstant: Optional[Any] = None
    specularExponent: Optional[Any] = None


@dataclass
class FeTile(Element):
    element_name = "feTile"
    pass


@dataclass
class FeTurbulence(Element):
    element_name = "feTurbulence"
    baseFrequency: Optional[str] = None
    numOctaves: Optional[Any] = None
    seed: Optional[Any] = None
    stitchTiles: Optional[Any] = None
    type: Optional[Any] = None
