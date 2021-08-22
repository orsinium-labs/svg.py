from enum import Enum


class FontStretch(Enum):
    NORMAL = "normal"
    WIDER = "wider"
    NARROWER = "narrower"
    ULTRA_CONDENSED = "ultra-condensed"
    EXTRA_CONDENSED = "extra-condensed"
    SEMI_CONDENSED = "semi-condensed"
    SEMI_EXPANDED = "semi-expanded"
    EXPANDED = "expanded"
    EXTRA_EXPANDED = "extra-expanded"
    ULTRA_EXPANDED = "ultra-expanded"
    INHERIT = "inherit"


class AngleUnit(Enum):
    DEG = "deg"
    GRAD = "grad"
    RAD = "rad"
    DEFAULT = ""


class LengthUnit(Enum):
    EM = "em"
    EX = "ex"
    PX = "px"
    PT = "pt"
    PC = "pc"
    CM = "cm"
    MM = "mm"
    IN = "in"
    PERCENT = "%"
    DEFAULT = ""


class BaselineShift(Enum):
    BASELINE = "baseline"
    SUB = "sub"
    SUPER = "super"
    INHERIT = "inherit"


class ClipFillRule(Enum):
    EVENODD = "evenodd"
    NONZERO = "nonzero"
    INHERIT = "inherit"


class CursorValue(Enum):
    AUTO = "auto"
    CROSSHAIR = "crosshair"
    DEFAULT = "default"
    POINTER = "pointer"
    MOVE = "move"
    E_RESIZE = "e-resize"
    NE_RESIZE = "ne-resize"
    NW_RESIZE = "nw-resize"
    N_RESIZE = "n-resize"
    SE_RESIZE = "se-resize"
    SW_RESIZE = "sw-resize"
    S_RESIZE = "s-resize"
    W_RESIZE = "w-resize"
    TEXT = "text"
    WAIT = "wait"
    HELP = "help"
    INHERIT = "inherit"


class EnableBackgroundValue(Enum):
    ACCUMULATE = "accumulate"
    X = "x"
    Y = "y"
    WIDTH = "width"
    HEIGHT = "height"
    INHERIT = "inherit"
    NEW = "new"


class PathTypeAbs(Enum):
    MOVETO = "M"
    LINETO = "L"
    HORIZONTAL_LINETO = "H"
    VERTICAL_LINETO = "V"
    CURVETO = "C"
    SMOOTH_CURVETO = "S"
    QUADRATIC_BEZIER_CURVETO = "Q"
    SMOOTH_QUADRATIC_BEZIER_CURVETO = "T"
    ARC_PATH = "A"
    CLOSE_PATH = "Z"


class PathTypeRel(Enum):
    MOVETO = "m"
    LINETO = "l"
    HORIZONTAL_LINETO = "h"
    VERTICAL_LINETO = "v"
    CURVETO = "c"
    SMOOTH_CURVETO = "s"
    QUADRATIC_BEZIER_CURVETO = "q"
    SMOOTH_QUADRATIC_BEZIER_CURVETO = "t"
    ARC_PATH = "a"
    CLOSE_PATH = "z"


class PreserveAspectRatioAlignment(Enum):
    """
    https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/preserveAspectRatio
    """
    NONE = "none"
    X_MIN_Y_MIN = "xMinYMin"
    X_MID_Y_MIN = "xMidYMin"
    X_MAX_Y_MIN = "xMaxYMin"
    X_MIN_Y_MID = "xMinYMid"
    X_MID_Y_MID = "xMidYMid"
    X_MAX_Y_MID = "xMaxYMid"
    X_MIN_Y_MAX = "xMinYMax"
    X_MID_Y_MAX = "xMidYMax"
    X_MAX_Y_MAX = "xMaxYMax"


class PreserveAspectRatioScaleType(Enum):
    MEET = "meet"
    SLICE = "slice"


class Spacing(Enum):
    AUTO = "auto"
    EXACT = "exact"


class TextDecoration(Enum):
    NONE = "none"
    UNDERLINE = "underline"
    OVERLINE = "overline"
    LINE_THROUGH = "line-through"
