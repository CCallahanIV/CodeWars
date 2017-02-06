"""This module containst the solution for the string pyramid kata.

http://www.codewars.com/kata/string-pyramid
"""


def watch_pyramid_from_the_side(characters):
    """Given a string of characters, make the triangle from the side."""
    if characters:
        space_count = 0
        count = len(characters)
        out_string = ""
        for char in characters:
            out_string += " " * space_count + char * (2 * count - 1) +\
                          " " * space_count + "\n"
            count -= 1
            space_count += 1
        return out_string[-2::-1]
    else:
        return characters


def watch_pyramid_from_above(characters):
    """Given a string of characters build a pyramid out of the characters."""
    if characters:
        rows = []
        for i in range(len(characters)):
            rows.append(characters[:i] + characters[i] * len(characters[i:]))
        for i in range(len(characters)):
            rows[i] += rows[i][-2::-1]
        for i in range(len(characters) - 2, -1, -1):
            rows.append(rows[i])
        return "\n".join(rows)
    else:
        return characters


def count_visible_characters_of_the_pyramid(characters):
    """Given a string of characters, find the number of visible chars in pyramid."""
    if characters:
        return (2 * len(characters) - 1) ** 2
    else:
        return -1


def count_all_characters_of_the_pyramid(characters):
    """Given a stirng of chars, find the total number of chars in the pyramid."""
    if characters:
        total = 0
        for i in range(len(characters)):
            total += count_visible_characters_of_the_pyramid(characters[i:])
        return total
    else:
        return -1
