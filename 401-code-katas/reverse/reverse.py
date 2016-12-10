"""This module contains the solution for the recursive revers string kata."""


def rec_reverse(s, rev=""):
    """Recursively reverses a string."""
    if len(s) == 0:
        return rev
    else:
        rev += s[-1]
        return rec_reverse(s[:-1], rev)
