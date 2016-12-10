"""This module contains the tests for mulitpes()."""

import pytest

TEST_PARAMS = [
    (2, 4, 40, [4, 8, 12, 16, 20, 24, 28, 32, 36]),
    (3, 4, 40, [12, 24, 36]),
    (7, 4, 80, [28, 56]),
    (7, 4, 20, [])
]


@pytest.mark.parametrize("n1, n2, end, result", TEST_PARAMS)
def test_mulitples(n1, n2, end, result):
    """Test output of filter_list() function"""
    from show_multipes import multiples
    assert multiples(n1, n2, end) == result
