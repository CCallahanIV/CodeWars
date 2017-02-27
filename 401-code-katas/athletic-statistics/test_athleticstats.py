import pytest

TEST_PARAMS = [
    (("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"), 
    ("Range: 01|01|18 Average: 01|38|05 Median: 01|32|34")),
    (("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"), 
    ("Range: 00|31|17 Average: 02|26|18 Median: 02|22|00"))
]


@pytest.mark.parametrize("test_param, expected", TEST_PARAMS)
def test_stats(test_param, expected):
    """Test the statistics for given input."""
    from athleticstats import stat
    assert stat(test_param) == expected
