"""This module contains the solution for the List Filtering Kata."""


def filter_list(lst):
    """Filter any non-int objects from a given list."""
    return [i for i in lst if type(i) == int]
