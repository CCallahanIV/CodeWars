"""This module contains the solution for the prefill kata."""
"""https://www.codewars.com/kata/54129112fb7c188740000162/train/python."""


def prefill(n, v="undefined"):
    """Given n and v, prefill a list n long with v."""
    if type(n) is not int:
        try:
            n = int(n)
        except ValueError:
            raise TypeError("{} is invalid".format(n))
        except TypeError:
            raise TypeError("{} is invalid".format(n))
    if n == 0:
        return []
    return [v] * n
