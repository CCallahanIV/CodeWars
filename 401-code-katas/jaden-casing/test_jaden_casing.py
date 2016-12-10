"""This module contains the tests for jaden_case()."""

import pytest

TEST_PARAMS = [
    ("How can mirrors be real if our eyes aren't real", "How Can Mirrors Be Real If Our Eyes Aren't Real"),
    ("", ""),
    ("TRY THIS", "Try This"),
    ("once more", "Once More")
]


@pytest.mark.parametrize("n, result", TEST_PARAMS)
def test_jaden_case(n, result):
    """Test output of jaden_case() function"""
    from jaden_casing import jaden_case
    assert jaden_case(n) == result
