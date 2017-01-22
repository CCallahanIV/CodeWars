"""This module contains the tests for the card sort kata."""


import pytest


TEST_PARAMS = [
    (list('39A5T824Q7J6K'), list('A23456789TJQK')),
    (list('Q286JK395A47T'), list('A23456789TJQK')),
    (list('54TQKJ69327A8'), list('A23456789TJQK')),
]


@pytest.mark.parametrize("qry, res", TEST_PARAMS)
def test_card_sort_pq(qry, res):
    """Test the card sort kata."""
    from card_sort import sort_cards_pq
    assert sort_cards_pq(qry) == res


@pytest.mark.parametrize("qry, res", TEST_PARAMS)
def test_card_sort(qry, res):
    """Test the card sort kata (non PQ solution)."""
    from card_sort import sort_cards
    assert sort_cards(qry) == res
