import pytest


TEST_PARAMS = [
    ("abBA", "AaBb"),
    ("AaaaaZazzz", "AaaaaaZzzz"),
    ("CbcBcbaA", "AaBbbCcc"),
    ("xXfuUuuF", "FfUuuuXx"),
    ("", ""),
    # ("ABbb", "ABbb"),
    # ('soZqoUrlkvnzFkflEinAwlWKzrqxixszisLewammvnoQwmnSlRgoriYxNGmvgwzMJoxVlzXzfiOmzlfiHixmyIxwgyi', 'AaEeFfffGgggHIiiiiiiiiJKkkLllllllMmmmmmmNnnnnOoooooQqqRrrrSsssUVvvvWwwwwwXxxxxxxYyyZzzzzzzz')
]


@pytest.mark.parametrize("qry, res", TEST_PARAMS)
def test_where_is_parent(qry, res):
    """Test the card sort kata."""
    from where_is_parent import find_children
    assert find_children(qry) == res
