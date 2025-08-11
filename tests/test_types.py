from datetime import datetime, timedelta

import pytest

from svg._types import to_clock_value, to_wallclock_sync_value


@pytest.mark.parametrize("input, expected", [
    # Timecount-val
    (timedelta(), "0s"),
    (timedelta(seconds=1), "1s"),
    (timedelta(seconds=-1), "-1s"),
    (timedelta(seconds=10), "10s"),
    (timedelta(seconds=-10), "-10s"),
    (timedelta(seconds=0.5), "0.5s"),
    (timedelta(seconds=-0.5), "-0.5s"),
    (timedelta(seconds=0.002), "0.002s"),
    (timedelta(seconds=-0.002), "-0.002s"),
    (timedelta(milliseconds=1), "0.001s"),
    (timedelta(milliseconds=-1), "-0.001s"),

    # Full-clock-val
    (timedelta(seconds=70), "0:01:10"),
    (timedelta(seconds=605), "0:10:05"),
    (timedelta(days=10), "240:00:00"),
    (timedelta(hours=5, minutes=7, seconds=12.2), "5:07:12.2"),
    (timedelta(hours=-1), "-1:00:00"),
])
def test_to_clock_value(input, expected):
    actual = to_clock_value(input)
    assert actual == expected


@pytest.mark.parametrize("input, expected", [
    (
        datetime(year=2025, month=7, day=9),
        "wallclock(2025-07-09 00:00:00)",
    ),
    (
        datetime(year=1999, month=1, day=1, hour=13, minute=37, second=12, microsecond=4000),
        "wallclock(1999-01-01 13:37:12.004000)",
    ),
])
def test_to_wallclock_sync_value(input, expected):
    actual = to_wallclock_sync_value(input)
    assert actual == expected
