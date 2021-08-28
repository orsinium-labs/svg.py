from decimal import Decimal
from typing import List, Tuple, Union
from dataclasses import dataclass

from typing_extensions import Literal


INHERIT = Literal["inherit"]
NONE = Literal["none"]
AUTO = Literal["auto"]


Number = Union[Decimal, float, int]


@dataclass
class Angle:
    value: Number
    unit: Literal["deg", "grad", "rad"]

    def __str__(self) -> str:
        return f"{self.value}{self.unit}"


@dataclass
class Length:
    value: Number
    unit: Literal["em", "ex", "px", "pt", "pc", "cm", "mm", "in"]

    def __str__(self) -> str:
        return f"{self.value}{self.unit}"


@dataclass
class PathData:
    type: Union[
        Literal["M", "L", "H", "V", "C", "S", "Q", "T", "A", "Z"],
        Literal["m", "l", "h", "v", "c", "s", "q", "t", "a", "z"],
    ]
    points: List[Number]

    def __str__(self) -> str:
        points = " ".join(str(p) for p in self.points)
        return f"{self.type} {points}"


@dataclass
class PreserveAspectRatio:
    alignment: Literal[
        "none",
        "xMinYMin",
        "xMidYMin",
        "xMaxYMin",
        "xMinYMid",
        "xMidYMid",
        "xMaxYMid",
        "xMinYMax",
        "xMidYMax",
        "xMaxYMax",
    ] = "xMidYMid"
    scale_type: Literal["meet", "slice"] = "meet"


@dataclass
class ViewBoxSpec:
    min_x: int
    min_y: int
    width: int
    height: int


# str
Clip = str
URI = str
ContentType = str
Color = str
FontFamily = str
LanguageCode = str
Paint = str
Script = str
StyleSheet = str
SVGColor = str

# alias
NumberOrPercentage = Number
StrokeMiterLimit = Number

# union
Coordinate = Union[Number, Length]
FontSize = Union[Length, INHERIT]
FontSizeAdjust = Union[Number, NONE, INHERIT]
Kerning = Union[Length, AUTO, INHERIT]
NumberOptionalNumber = Union[Number, Tuple[Number, Number]]
Opacity = Union[Number, INHERIT]
StrokeDashArray = Union[str, List[Number]]
StrokeDashOffset = Union[NONE, Length]
StrokeWidth = Union[Number, Length]
Rotation = Union[Number, AUTO, Literal["auto-reverse"]]

# str union
ClipPath = Union[URI, AUTO, INHERIT, NONE]
Cursor = Union[
    URI,
    Literal[
        "auto",
        "crosshair",
        "default",
        "pointer",
        "move",
        "e-resize",
        "ne-resize",
        "nw-resize",
        "n-resize",
        "se-resize",
        "sw-resize",
        "s-resize",
        "w-resize",
        "text",
        "wait",
        "help",
        "inherit",
    ],
]
EnableBackground = Union[
    URI, Literal["accumulate", "x", "y", "width", "height", "inherit", "new"]
]
Filter = Union[URI, INHERIT, NONE]
Marker = Union[URI, NONE, INHERIT]
Mask = Union[URI, NONE, INHERIT]
Side = Literal["left", "right"]

# list of strings
Classes = List[str]
Extensions = List[str]
Features = List[str]
MediaDesc = List[str]
Transforms = List[str]

# lists
Coordinates = List[Coordinate]
LanguageCodes = List[LanguageCode]
Lengths = List[Length]
Numbers = List[Number]
Points = List[Number]
