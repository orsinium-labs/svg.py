from decimal import Decimal
from typing import List, Tuple, Union
from dataclasses import dataclass

from typing_extensions import Literal

from . import enums


INHERIT = Literal["inherit"]
NONE = Literal["none"]
AUTO = Literal["auto"]


Number = Union[Decimal, float, int]


@dataclass
class Angle:
    value: Number
    unit: enums.AngleUnit = enums.AngleUnit.DEFAULT

    def __str__(self) -> str:
        return f'{self.value}{self.unit.value}'


@dataclass
class Length:
    value: Number
    unit: enums.LengthUnit = enums.LengthUnit.DEFAULT

    def __str__(self) -> str:
        return f'{self.value}{self.unit.value}'


@dataclass
class PathData:
    type: Union[enums.PathTypeAbs, enums.PathTypeRel]
    points: List[Number]

    def __str__(self) -> str:
        points = ' '.join(str(p) for p in self.points)
        return f'{self.type.value} {points}'


@dataclass
class PreserveAspectRatio:
    alignment: enums.PreserveAspectRatioAlignment = enums.PreserveAspectRatioAlignment.X_MID_Y_MID
    scale_type: enums.PreserveAspectRatioScaleType = enums.PreserveAspectRatioScaleType.MEET


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
GlyphOrientationHorizontal = Union[Angle, INHERIT]
GlyphOrientationVertical = Union[Angle, INHERIT, AUTO]
Kerning = Union[Length, AUTO, INHERIT]
NumberOptionalNumber = Union[Number, Tuple[Number, Number]]
Opacity = Union[Number, INHERIT]
Spacing = Union[Length, AUTO, Literal["exact"]]
StrokeDashArray = Union[str, List[Number]]
StrokeDashOffset = Union[NONE, Length]
StrokeWidth = Union[Number, Length]

# str union
ClipPath = Union[URI, AUTO, INHERIT, NONE]
Cursor = Union[URI, enums.CursorValue]
EnableBackground = Union[URI, enums.EnableBackgroundValue]
Filter = Union[URI, INHERIT, NONE]
Marker = Union[URI, NONE, INHERIT]
Mask = Union[URI, NONE, INHERIT]

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
