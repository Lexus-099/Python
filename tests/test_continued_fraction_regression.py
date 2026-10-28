"""Regression tests for exact integer arithmetic in continued fractions."""

from fractions import Fraction

from maths.continued_fraction import continued_fraction


def test_large_integer_keeps_exact_value() -> None:
    value = 2**53 + 3
    assert continued_fraction(Fraction(value)) == [value]


def test_very_large_fraction_does_not_overflow_float_conversion() -> None:
    value = Fraction(10**400, 3)
    assert continued_fraction(value) == [10**400 // 3, 3]


def test_negative_fraction_keeps_floor_semantics() -> None:
    assert continued_fraction(Fraction("-2.25")) == [-3, 1, 3]
