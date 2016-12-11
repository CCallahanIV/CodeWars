"""This file contains the Array.diff codewars solution."""


def array_diff(a, b):
    """Return a list of a - b."""
    c = [i for i in a if i not in b]
    return c
