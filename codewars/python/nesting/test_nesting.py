"""Tests for nesting.py."""

import pytest

TEST_CASES = [
    (([ 1, 1, 1 ], [ 2, 2, 2 ]), True),
    (([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ]), True),
    (([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ]), False),
    (([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ]), False),
    (([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ]), True),
    (([ [ [ ], [ ] ] ], [ [ 1, 1 ] ]), False) 
]

@pytest.mark.parametrize("test_data, exp", TEST_CASES)
def test_same_structure_as(test_data, exp):
    """Test the same_structure_as function."""
    from nesting import same_structure_as
    assert same_structure_as(test_data[0], test_data[1]) is exp