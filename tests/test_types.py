from datetime import datetime, timedelta

import pytest

from svg._types import to_clock_value, to_wallclock_sync_value


clock_values = [
    (timedelta(seconds=10), "0:00:10"),
    (timedelta(seconds=70), "0:01:10"),
    (timedelta(seconds=0.5), "0:00:00.5"),
    (timedelta(days=10), "240:00:00"),
    (timedelta(hours=5, minutes=7, seconds=12.2), "5:07:12.2"),
    (timedelta(hours=-1), "-1:00:00"),
    (timedelta(seconds=-0.002), "-0:00:00.002"),
    (timedelta(milliseconds=-1), "-0:00:00.001"),
]


@pytest.mark.parametrize("input, expected", clock_values)
def test_to_clock_value(input, expected):
    actual = to_clock_value(input)
    assert actual == expected


wallclock_values = [
    (datetime(year=2025, month=7, day=9), "wallclock(2025-07-09 00:00:00)"),
    (datetime(year=1999, month=1, day=1, hour=13, minute=37, second=12, microsecond=4000), "wallclock(1999-01-01 13:37:12.004000)"),
]

@pytest.mark.parametrize("input, expected", wallclock_values)
def test_to_wallclock_sync_value(input, expected):
    actual = to_wallclock_sync_value(input)
    assert actual == expected
