"""This file contains the function for the sum of nth series codewars
problem.
"""


def series_sum(n):
    """Given n, return sum of series up to nth term.  n = 0 returns 0"""
    sum_series = 0.0
    for i in range(1, n + 1):
        sum_series += 1 / (3 * (float(i) - 1) + 1)

    return '{:.2f}'.format(sum_series)
