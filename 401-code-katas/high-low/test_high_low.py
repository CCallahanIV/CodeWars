"""This file contains the tests for the high_and_low() function."""

import pytest

TEST_PARAMS = [
    ("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6", "542 -214"),
    ("1 -1", "1 -1"),
    ("1 1", "1 1"),
    ("-1 -1", "-1 -1"),
    ("1 -1 0", "1 -1"),
    ("1 1 0", "1 0"),
    ("-1 -1 0", "0 -1"),
    ("42", "42 42")
]


@pytest.mark.parametrize("n, result", TEST_PARAMS)
def test_series_sum(n, result):
    """Test output of sum_series() function"""
    from high_low import high_and_low
    assert high_and_low(n) == result
