"""This module contains the solution for the CF 401 Proper Parenthetics assignment."""

from queue import Queue


def proper_parenthetics(test_str):
    """Test for proper parenthetics in a given string."""
    q = Queue(test_str)

    num_opening = 0
    num_closing = 0

    while len(q) > 0:
        char = q.dequeue()
        if char == ')' and num_opening <= num_closing:
            return -1
        elif char == '(':
            num_opening += 1
        elif char == ')':
            num_closing += 1

    if num_opening > num_closing:
        return 1
    else:
        return 0
