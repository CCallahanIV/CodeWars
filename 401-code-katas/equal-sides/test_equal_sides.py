"""This module contains the tests for find_even_index()."""

import pytest

TEST_PARAMS = [
    ([1, 2, 3, 4, 3, 2, 1], 3),
    ([1, 100, 50, -51, 1, 1], 1,),
    ([1, 2, 3, 4, 5, 6], -1),
    ([20, 10, 30, 10, 10, 15, 35], 3),
    ([20, 10, -80, 10, 10, 15, 35], 0),
    ([10, -80, 10, 10, 15, 35, 20], 6),
    (range(1, 100), -1),
    ([0, 0, 0, 0, 0], 0),#"Should pick the first index if more cases are valid"
    ([-1, -2, -3, -4, -3, -2, -1], 3),
    (range(-100, -1), -1)
]


@pytest.mark.parametrize("n, result", TEST_PARAMS)
def test_equal_sides(n, result):
    """Test output of find_even_index() function"""
    from equal_sides import find_even_index
    assert find_even_index(n) == result
