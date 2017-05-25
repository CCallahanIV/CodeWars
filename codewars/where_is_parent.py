"""
Code wars Kata

Mothers arranged dance party for children in school.On that party there are 
only mothers and their children.All are having great fun on dancing floor when 
suddenly all lights went out.Its dark night and no one can see eachother.But 
you were flying nearby and you can see in the dark and have ability to 
teleport people anywhere you want.

Legend:

-Uppercase letters stands for mothers,lowercase stand for their children. 
I.E "A" mothers children are "aaaa".

-Function input:String contain only letters,Uppercase letters are unique.
Task:

Place all people in alphabetical order where Mothers are followed by 
their children.I.E "aAbaBb" => "AaaBbb".
"""


def find_children(families):
    """
    Given a string of capital and lower case letters, return sorted string
    with capital letters leading same lower case letters.
    """

    families_dict = {}

    for char in families:
        if char.istitle():
            families_dict[char].setdefault(char, 0)
        else:
            families_dict[char.upper()] = families_dict[char.upper()].setdefault(char.upper(), 0) + 1

    found_families = []
    for parent, children in families_dict.items():
        found_families.append(parent + children * parent.lower())
    return "".join(sorted(found_families))

