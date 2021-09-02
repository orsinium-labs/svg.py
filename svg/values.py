from decimal import Decimal
from typing import List, Tuple, Union
from dataclasses import dataclass

from typing_extensions import Literal


INHERIT = Literal["inherit"]
NONE = Literal["none"]


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
URI = str
ContentType = str
StyleSheet = str

# union
Coordinate = Union[Number, Length]
FontSize = Union[Length, INHERIT]
FontSizeAdjust = Union[Number, NONE, INHERIT]
NumberOptionalNumber = Union[Number, Tuple[Number, Number]]
Opacity = Union[Number, INHERIT]
StrokeDashArray = Union[str, List[Number]]

# str union
ClipPath = Union[URI, Literal["auto"], INHERIT, NONE]
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
Marker = Union[URI, NONE, INHERIT]
Mask = Union[URI, NONE, INHERIT]

# list of strings
Classes = List[str]

# lists
Coordinates = List[Coordinate]
Lengths = List[Length]
Numbers = List[Number]
Points = List[Number]

AlignmentBaseline = Literal[
    "baseline",
    "top",
    "before-edge",
    "text-top",
    "text-before-edge",
    "middle",
    "bottom",
    "after-edge",
    "text-bottom",
    "text-after-edge",
    "ideographic",
    "lower",
    "hanging",
    "mathematical",
    "inherit",
]
