"""Testing the proper paranthetics function, CF 401 Python assignment."""

import pytest

TEST_PARAMS = [
    ("(sometext)", 0),
    ("(sometext", 1),
    (")sometext)", -1),
    ("(sometext(", 1),
    ("sometext)", -1),
    ("(sometext))", -1),
    ("(Something)(more complicated)", 0),
    ("(something(even more( complicated)", 1),
    ("(Something(so )() unbalanced", 1),
    (")((((((something)))))", -1),
    ("(((())", 1)
]

@pytest.mark.parametrize("test_str, result", TEST_PARAMS)
def test_proper_parenthetics(test_str, result):
    """Test the proper_parenthetics function."""
    from proper_parenthetics import proper_parenthetics
    assert proper_parenthetics(test_str) == result

