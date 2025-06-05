# test Length class operations
from decimal import Decimal 
import pytest
from svg._types import Length

@pytest.mark.parametrize(
    "op, length1, length2, expected",
    [
        ("+", Length(10, "px"), Length(5, "px"), Length(15, "px")),
        ("-", Length(10, "px"), Length(5, "px"), Length(5, "px")),
        ("*", Length(10, "px"), 2, Length(20, "px")),
        ("/", Length(10, "px"), 2, Length(5, "px")),
        ("neg", Length(10, "px"), None, Length(-10, "px")),
        ("+", Length(10, "px"), 5.0, Length(15.0, "px")),
        ("-", 10.0, Length(5, "px"), Length(5.0, "px")),
        ("*", 5.0, Length(10, "px"), Length(50.0, "px")),
        ("/", Length(10, "px"), 3.0, Length(10.0/3, "px")),
        ("neg", Length(10, "px"), None, Length(-10, "px")),
        ("+", Length(Decimal("10.5"), "px"), Length(Decimal("5.5"), "px"), Length(Decimal("16.0"), "px")),
        ("-", Length(Decimal("10.5"), "px"), Length(Decimal("5.5"), "px"), Length(Decimal("5.0"), "px")),
        ("*", Length(Decimal("10.5"), "px"), Decimal("2.0"), Length(Decimal("21.0"), "px")),
        ("/", Length(Decimal("10.5"), "px"), Decimal("2.0"), Length(Decimal("5.25"), "px")),
    ]
)
def test_length_operations(op, length1, length2, expected):
    if op == "+":
        assert length1 + length2 == expected
    elif op == "-":
        assert length1 - length2 == expected
    elif op == "*":
        assert length1 * length2 == expected
    elif op == "/":
        assert length1 / length2 == expected
    elif op == "neg":
        assert -length1 == expected
    else:
        raise ValueError("Unknown operation")


@pytest.mark.parametrize(
    "op, length1, length2, expected_exception",
    [
        ("+", Length(10, "px"), Length(5, "em"), ValueError),
        ("-", Length(10, "px"), Length(5, "em"), ValueError),
        ("*", Length(10, "px"), Length(5, "em"), TypeError),
        ("/", Length(10, "px"), Length(5, "em"), TypeError),
        ("+", Length(Decimal(10), "px"), Length(5.2, "px"), TypeError),  #decimal with float
        ("-", Length(Decimal(10), "px"), Length(5.2, "px"), TypeError),  #decimal with float
        ("*", Length(Decimal(10), "px"), Length(5.2, "px"), TypeError),  #decimal with float
        ("/", Length(Decimal(10), "px"), Length(5.2, "px"), TypeError),  #decimal with float
        ("+", Length(Decimal(10), "px"), 5.5, TypeError),  #decimal with different unit
        ("-", Length(Decimal(10), "px"), 5.5, TypeError),  #decimal with different unit
        ("*", Length(Decimal(10), "px"), 5.5, TypeError),  #decimal with different unit
        ("/", Length(Decimal(10), "px"), 5.5, TypeError),  #decimal with different unit
    ]
)
def test_length_exceptions(op, length1, length2, expected_exception):
    with pytest.raises(expected_exception):
        if op == "+":
            _ = length1 + length2
        elif op == "-":
            _ = length1 - length2
        elif op == "*":
            _ = length1 * length2
        elif op == "/":
            _ = length1 / length2