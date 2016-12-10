"""This module contains the tests for flatten_me()."""

import pytest

TEST_PARAMS = [
    ([1, [2, 3], 4], [1, 2, 3, 4]),
    ([['a', 'b'], 'c', ['d']], ['a', 'b', 'c', 'd']),
    (['!', '?'], ['!', '?']),
    ([[True, False], ['!'], ['?'], [71, '@']], [True, False, '!', '?', 71, '@'])
]


@pytest.mark.parametrize("n, result", TEST_PARAMS)
def test_flatten_me(n, result):
    """Test output of flatten_me() function"""
    from flatten import flatten_me
    assert flatten_me(n) == result
