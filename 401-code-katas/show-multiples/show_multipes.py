"""This module contains the solution for the Show Multiples kata."""

def multiples(n1, n2, end):
    """Return list of numbers for which both n1 and n2 are a multiple up to end."""
    return [i for i in range(1, end) if i % n1 == 0 and i % n2 == 0]
