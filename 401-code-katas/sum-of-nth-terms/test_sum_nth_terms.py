"""Test series_sum()"""
import pytest


TEST_PARAMS = [
    (0, "0.00"),
    (1, "1.00"),
    (2, "1.25"),
    (3, "1.39")
]


@pytest.mark.parametrize("n, result", TEST_PARAMS)
def test_series_sum(n, result):
    """Test output of sum_series() function"""
    from sum_nth_terms import series_sum
    assert series_sum(n) == result
