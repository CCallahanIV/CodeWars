"""This module contains the tests for rec_reverse()."""

import pytest

TEST_PARAMS = [
    "hello world",
    "try this",
    "another string",
    "",
    "d"
]


@pytest.mark.parametrize("n", TEST_PARAMS)
def test_rec_reverse(n):
    """Test output of rec_reverse() function"""
    from reverse import rec_reverse
    assert rec_reverse(n) == n[::-1]
