"""
Raj was to move up through a pattern of stairs of a given number (n). Help him to get to the top using the function stairs.

##Keep in mind :

If n<1 then return ' ' .
There are a lot of spaces before the stair starts except for pattern(1)
##Examples : pattern(1)

      1 1
pattern(6)

                      1 1
                  1 2 2 1  
              1 2 3 3 2 1
          1 2 3 4 4 3 2 1
      1 2 3 4 5 5 4 3 2 1
  1 2 3 4 5 6 6 5 4 3 2 1

"""

def stairs(n):
    """Given integer n, print the correct stairs."""
    if n < 1:
        return ' '
    output_stairs = ''
    for i in range(1, n + 1):
        # Add leading white space
        output_stairs += '    ' * (n - i)
        # Add numbers
        num_list = [ str(i % 10) for i in range(1, i + 1) ]
        output_stairs += ' '.join(num_list) + ' ' + ' '.join(reversed(num_list))
        # Add new line, except last line.
        if i < n:
            output_stairs += '\n'

    return output_stairs
