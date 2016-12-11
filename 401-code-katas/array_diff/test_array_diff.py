"""This module contains the tests for array_diff()."""

import pytest

TEST_PARAMS = [
    (([1, 2], [1]), [2]),
    (([1, 2, 2], [1]), [2, 2]),
    (([1, 2, 2], [2]), [1]),
    (([1, 2, 2], []), [1, 2, 2]),
    (([], [1, 2]), [])
]


@pytest.mark.parametrize("n, result", TEST_PARAMS)
def test_array_diff(n, result):
    """Test output of sum_series() function"""
    from array_diff import array_diff
    a, b = n
    assert array_diff(a, b) == result
