from __future__ import annotations
from ._types import Length, Number


def escape(text: str) -> str:
    """Make the text safe to use in SVG.
    """
    text = text.replace("&", "&amp;")
    text = text.replace(">", "&gt;")
    text = text.replace("<", "&lt;")
    return text


def mm(val: Number) -> Length:
    """Explicitly specify mm unit for the value.
    """
    return Length(value=val, unit='mm')


def px(val: Number) -> Length:
    """Explicitly specify px unit for the value.
    """
    return Length(value=val, unit='px')
