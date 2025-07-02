import pytest

from svg._types import ClockValue


# https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/Content_type#clock-value
test_values = [
    ("02:30:03", ClockValue(3, 30, 2)),
    ("50:00:10.25", ClockValue(10.25, 0, 50)),
    ("02:33", ClockValue(33, 2)),
    ("00:10.5", ClockValue(10.5)),
    ("3.2h", ClockValue(0, 12, 3)),
    ("45min", ClockValue(0, 45)),
    ("30s", ClockValue(30)),
    ("5ms", ClockValue(0.005)),
    ("12.467", ClockValue(12.467)),
    ("00.5", ClockValue(0.5)),
    ("00:00.005", ClockValue(0.005)),
]


@pytest.mark.parametrize("string, expected", test_values)
def test_clock_value(string, expected):
    actual = ClockValue.from_str(string)
    assert actual == expected

