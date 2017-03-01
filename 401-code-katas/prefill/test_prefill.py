"""This module contains the tests for the prefill kata."""

import pytest
from prefill import prefill

BASE_CASES = [
    ((3, 1), [1, 1, 1]),
    ((2, 'abc'), ['abc', 'abc']),
    (('1', 1), [1]),
    ((3, prefill(2, '2d')), [['2d', '2d'], ['2d', '2d'], ['2d', '2d']]),
]

ERROR_CASES = [
    ('xyz', 1),
]


def test_base_cases():
    """Test prefill for all base cases."""
    for test in BASE_CASES:
        assert prefill(test[0][0], test[0][1]) == test[1]


def test_error_cases():
    """Test prefill for error cases."""
    for test in ERROR_CASES:
        with pytest.raises(TypeError):
            prefill(test[0][0], test[0][1])
