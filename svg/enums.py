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


class TextDecoration(Enum):
    NONE = "none"
    UNDERLINE = "underline"
    OVERLINE = "overline"
    LINE_THROUGH = "line-through"


class ColorInterpolation(Enum):
    AUTO = "auto"
    SRGB = "sRGB"
    LINEAR_RGB = "linearRGB"
    INHERIT = "inherit"


class Rendering(Enum):
    AUTO = "auto"
    OPTIMIZE_SPEED = "optimizeSpeed"
    OPTIMIZE_QUALITY = "optimizeQuality"
    INHERIT = "inherit"


class LineCap(Enum):
    BUTT = "butt"
    ROUND = "round"
    SQUARE = "square"
    INHERIT = "inherit"


class LineJoin(Enum):
    MITER = "miter"
    ROUND = "round"
    BEVEL = "bevel"
    INHERIT = "inherit"


class FontStyle(Enum):
    NORMAL = "normal"
    ITALIC = "italic"
    OBLIQUE = "oblique"
    INHERIT = "inherit"


class FontValiant(Enum):
    NORMAL = "normal"
    SMALL_CAPS = "small-caps"
    INHERIT = "inherit"


class FontWeight(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    BOLDER = "bolder"
    LIGHTER = "lighter"
    V100 = "100"
    V200 = "200"
    V300 = "300"
    V400 = "400"
    V500 = "500"
    V600 = "600"
    V700 = "700"
    V800 = "800"
    V900 = "900"
    INHERIT = "inherit"


class Visibility(Enum):
    VISIBLE = "visible"
    HIDDEN = "hidden"
    INHERIT = "inherit"


class TextAlignment(Enum):
    BASELINE = "baseline"
    TOP = "top"
    BEFORE_EDGE = "before-edge"
    TEXT_TOP = "text-top"
    TEXT_BEFORE_EDGE = "text-before-edge"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    AFTER_EDGE = "after-edge"
    TEXT_BOTTOM = "text-bottom"
    TEXT_AFTER_EDGE = "text-after-edge"
    IDEOGRAPHIC = "ideographic"
    LOWER = "lower"
    HANGING = "hanging"
    MATHEMATICAL = "mathematical"
    INHERIT = "inherit"


class TextDirection(Enum):
    LTR = "ltr"
    RTL = "rtl"
    INHERIT = "inherit"


class DominantBaseline(Enum):
    AUTO = "auto"
    AUTOSENSE_SCRIPT = "autosense-script"
    NO_CHANGE = "no-change"
    RESET = "reset"
    IDEOGRAPHIC = "ideographic"
    LOWER = "lower"
    HANGING = "hanging"
    MATHEMATICAL = "mathematical"
    INHERIT = "inherit"


class TextAnchor(Enum):
    START = "start"
    MIDDLE = "middle"
    END = "end"
    INHERIT = "inherit"


class Overflow(Enum):
    VISIBLE = "visible"
    HIDDEN = "hidden"
    SCROLL = "scroll"
    AUTO = "auto"
    INHERIT = "inherit"


class ComponentTransferType(Enum):
    IDENTITY = "identity"
    TABLE = "table"
    DISCRETE = "discrete"
    LINEAR = "linear"
    GAMMA = "gamma"


class ZoomAndPan(Enum):
    DISABLE = "disable"
    MAGNIFY = "magnify"
    ZOOM = "zoom"


class TransformType(Enum):
    TRANSLATE = "translate"
    SCALE = "scale"
    ROTATE = "rotate"
    SKEWX = "skewX"
    SKEWY = "skewY"
