"""This module contains the solution for the Equal Sides of An Array kata."""


def find_even_index(arr):
    """Given an array, find an index for which the sum of the sublists on each side are equal."""
    flag = -1
    for i in range(len(arr)):
        left = arr[:i]
        right = arr[i + 1:]
        if sum(left) == sum(right):
            flag = i
            break
    return flag
