"""This method contains the solution the flatten me kata."""


def flatten_me(lst, new_lst=None):
    """Given any list, flatten the contents to single level list."""
    if new_lst is None:
        new_lst = []

    for item in lst:
        if isinstance(item, list):
            flatten_me(item, new_lst)
        else:
            new_lst.append(item)

    return new_lst
