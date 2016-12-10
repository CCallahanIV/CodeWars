"""Solution to the Jaden Casing kata."""


def jaden_case(s):
    """Jaden Case any given string (first letter of each word capitalized)"""
    lst_s = s.split()
    for i in range(len(lst_s)):
        lst_s[i] = lst_s[i].lower().capitalize()
    return " ".join(lst_s)
