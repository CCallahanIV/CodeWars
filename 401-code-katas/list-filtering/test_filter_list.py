"""This module contains the tests for filter_list()."""

import pytest

TEST_PARAMS = [
    ([1, 2, 'a', 'b'], [1, 2]),
    ([1, 'a', 'b', 0, 15], [1, 0, 15]),
    ([1, 2, 'aasf', '1', '123', 123], [1, 2, 123]),
    ([True, False, 1, 2, 'string'], [1, 2])
]


@pytest.mark.parametrize("n, result", TEST_PARAMS)
def test_filter_list(n, result):
    """Test output of filter_list() function"""
    from filter_list import filter_list
    assert filter_list(n) == result
