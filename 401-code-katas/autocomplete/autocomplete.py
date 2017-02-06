"""A trie data structure implemented as a class."""

from trie import Trie


class AutoCompleter(object):
    """
    Trie class.

    __init__:
    insert(string): adds a string to the trie.
    contains(string): returns true if string is in the trie, else false.
    size(): returns the number of words in the trie. 0 if empty.
    remove(string): will remove the string from the trie. Exception otherwise.
    """

    def __init__(self, vocabulary, max_completions=4):
        """Initialize the Trie class."""
        self._container = Trie()
        self.max_completions = max_completions
        if type(vocabulary) is str:
            self._init_with_file(vocabulary)
        else:
            try:
                for word in vocabulary:
                    self._container.insert(word)
            except IndexError:
                raise TypeError("Improper format, please initialize with filename or list of words.")

    def _init_with_file(self, file_path):
        """Given a file name, initialize AutoCompleter with contents."""
        with open(file_path, 'r') as f:
            vocab = f.readlines()
        for word in vocab:
            self._container.insert(word.strip())

    # def complete_me(self, prefix):
    #     """Given a prefix string, provide max_completions complete words for the string."""
    #     start_node = self._container.root
    #     for char in prefix:
    #         if char in start_node.children:
    #             start_node = start_node.children[char]
    #         else:
    #             raise ValueError("That string is not in this Trie.")

    #     word_list = []
    #     trav_list = []
    #     pref_list = []
    #     for i, (key, node) in enumerate(reversed(start_node.children.items())):
    #         trav_list.append((key, node))
    #     pref_list.append(prefix)
    #     word = prefix
    #     while trav_list:
    #         curr = trav_list.pop()
    #         word += curr[0]
    #         if len(word_list) == self.max_completions:
    #             return word_list

    #         if curr[1].end and curr[1].children:
    #             word_list.append(word)

    #         if not curr[1].children:
    #             word_list.append(word)
    #             word = pref_list.pop()

    #         elif len(curr[1].children) > 1:
    #             for child in curr[1].children:
    #                 pref_list.append(word)

    #         start_node = curr[1]
    #         for i, (key, node) in enumerate(reversed(start_node.children.items())):
    #             trav_list.append((key, node))

    #     return word_list

    def complete_me(self, prefix):
        start_node = self._container.root
        for char in prefix:
            if char in start_node.children:
                start_node = start_node.children[char]
            else:
                raise ValueError("That string is not in this Trie.")
        word_lst = self._traverse(prefix, start_node, [])
        return word_lst

    def _traverse(self, prefix, curr_node, word_lst):
        """Given a prefix and current node, traverse tree.  Return prefix if node has no children."""
        print(word_lst)
        if curr_node.end or not curr_node.children:
            word_lst.append(prefix)

        if len(word_lst) >= self.max_completions:
            return word_lst

        for i, (key, node) in enumerate(curr_node.children.items()):
            new_pref = prefix + key
            self._traverse(new_pref, node, word_lst)
        return word_lst
