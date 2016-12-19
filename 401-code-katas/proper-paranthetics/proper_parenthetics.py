"""This module contains the solution for the CF 401 Proper Parenthetics assignment."""

from queue import Queue
import sys


def proper_parenthetics(test_str):
    """Test for proper parenthetics in a given string."""
    if sys.version_info[0] < 3:
        q = Queue(list(test_str))
    else:
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

    return 1 if num_opening > num_closing else 0
