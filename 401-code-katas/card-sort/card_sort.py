"""This module contains the solution for the card sorting kata.

https://www.codewars.com/kata/sort-deck-of-cards/train/python
"""


from binheap_pq import PriorityQBinHeap


def sort_cards_pq(lst):
    """Given a list of cards, sort and return the cards as a list, using a Priority Q."""
    ref_dict = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6,
                '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12,
                }

    p = PriorityQBinHeap()

    for card in lst:
        p.push(card, ref_dict[card])

    out_lst = [p.pop()[0] for i in range(len(p))]

    return out_lst


def sort_cards(lst):
    """Given a list of cards, sort and return the cards as a list."""
    ref_dict = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6,
                '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12,
                }

    card_lst = [(card, ref_dict[card]) for card in lst]
    card_lst.sort(key=lambda x: x[1])

    return [card[0] for card in card_lst]
