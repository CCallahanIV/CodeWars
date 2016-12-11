"""This file contains the solution for the high_low kata
url: https://www.codewars.com/kata/highest-and-lowest/train/python

"""


def high_and_low(numbers):
    """Return the highest and lowest numbers in given string of numbers."""
    num_lst = [int(num) for num in numbers.split()]
    num_lst = sorted(num_lst, reverse=True)
    return str(num_lst[0]) + " " + str(num_lst[-1])
