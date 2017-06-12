"""Complete the method (or function in Python) to return true when its argument is an array that has the same nesting structure as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""

def same_structure_as(original, other):
    """Return if original and other have same nesting structure, order matters."""

    if type(original) is not list or type(other) is not list:
        return False
    elif len(original) != len(other):
        return False
    for a, b in zip(original, other):
        if type(a) is list or type(b) is list:
            if type(a) is not type(b):
                return False
        if type(a) is list and type(b) is list:
            if not same_structure_as(a, b):
                return False

