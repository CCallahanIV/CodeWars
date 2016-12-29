# CodeWars

This repo contains all kata's completed from the Code Wars website


#Card Sort
 - Modules: binheap_pq.py, card_sort.py
 - Tests: test_card_sort.py
 - Link: https://www.codewars.com/kata/sort-deck-of-cards/python
 - The stretch goal for this kata was to use a Priority Queue Data Structure in order to solve it.  I did so by creating a reference dictionary of all the cards and their relative priorities.  Each card was pushed into the PQ and heap sorted by its priority.  Once all were inserted, they could all be popped into a list in sorted order to return.

#Sum of the nth term of Series
 - Module: sum_nth_terms.py
 - Tests: test_sum_nth_terms.py
 - Link: https://www.codewars.com/kata/555eded1ad94b00403000071

#Proper Parenthetics
 - Module: proper_parenthetics.py
 - Tests: test_paranthetics.py
 - Dependencies: dbl_linked_list.py and queue.py
 - Link: https://codefellows.github.io/sea-python-401d5/assignments/proper_parenthetics.html
 - A requirement for solving this problem was using a data structure that we had built.  I elected to use a queue because of its FIRST IN FIRST OUT access to data.  This way, I was able to read the given strings "left to right."
 

#BEGIN SNOW DAY:

1. Highest and Lowest
  - Module: high_low.py
  - Tests: test_high_low.py
  - Link: https://www.codewars.com/kata/highest-and-lowest/train/python

```
python

def high_and_low(numbers):
  """solution by: Azuaron, GNX, Zoran"""
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))
```

2. Array.Diff
  - Module: array_diff.py
  - Tests: test_array_diff.py
  - Link: https://www.codewars.com/kata/array-dot-diff/train/python

```
python
def array_diff(a, b):
    """solution by: douglasvaghetti"""
    return filter(lambda i: i not in b, a)
```

3. Recursive Reverse String
  - Module: reverse.py
  - Tests: test_reverse.py
  - Link: https://www.codewars.com/kata/recursive-reverse-string/train/python
NOTE: Testing requires that the recursive function is called recursively n times if n
is the length of the string.  I can complete the task with n + 1 recursive calls.
I would like help to figure out how to get it down to n.

```
python
def reverse(str):
  """solution by: BilboSwaggins"""
  return str[-1] + reverse(str[:-1]) if len(str) > 1 else str
```

4. Flatten Me
  - Module: flatten.py
  - Tests: test_flatten.py
  - Link: https://www.codewars.com/kata/flatten-me/train/python
  - was close to answer, this helped:
http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python

```
python
def _flat(a):
    for e in a:
        try:
            yield from e
        except TypeError:
            yield e

def flatten_me(lst):
    return list(_flat(lst))
```

5. Equal Sides of an Array
  - module: equal_sides.py
  - tests: test_equal_sides.py
  - Link:https://www.codewars.com/kata/equal-sides-of-an-array/train/python
```
python
def find_even_index(arr):
    left_sum, right_sum = 0, sum(arr)

    for i, n in enumerate(arr):
        right_sum -= n
        if left_sum == right_sum:
            return i
        left_sum += n

    return -1
```

6. List Filtering
  - module: filter_list.py
  - tests: test_filter_list.py
  - Link:https://www.codewars.com/kata/list-filtering/train/python
```
python
def filter_list(l):
  return filter(lambda x: not type(x) is str, l)
```

7. Show Multiples
  - module: show_multipes.py
  - tests: test_show_multiples.py
  - link: https://www.codewars.com/kata/show-multiples-of-2-numbers-within-a-range/train/python
```
python
def multiples(s1,s2,s3):
    """solution by narayanswa30663"""
    return filter(lambda i: not i % s1 and not i % s2, range(1, s3))
```

8. Jaden Casing
  - module: jaden_casing.py
  - tests: test_jaden_casing.py
  - links: https://www.codewars.com/kata/jaden-casing-strings/train/python

```
python
def toJadenCase(string):        
"""solution by Azuaron"""
    return " ".join(w.capitalize() for w in string.split())
```
