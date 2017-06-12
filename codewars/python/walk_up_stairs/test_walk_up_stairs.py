import pytest

TEST_CASES = [
    (3, "        1 1\n    1 2 2 1\n1 2 3 3 2 1"),
    (7, "                        1 1\n                    1 2 2 1\n                1 2 3 3 2 1\n            1 2 3 4 4 3 2 1\n        1 2 3 4 5 5 4 3 2 1\n    1 2 3 4 5 6 6 5 4 3 2 1\n1 2 3 4 5 6 7 7 6 5 4 3 2 1")
]

@pytest.mark.parametrize("n, exp", TEST_CASES)
def test_stairs(n, exp):
    """Test the stairs function."""
    from walk_up_stairs import stairs
    assert stairs(n) == exp