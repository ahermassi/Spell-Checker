class TrieNode:
    """ TrieNode holds information about the children of node and whether the node is the
        end of a word.
    """

    def __init__(self):
        self.children = dict()
        self.end_of_word = False

    def __getitem__(self, key):
        if key in self.children:
            return self.children[key]
        return None

    def __setitem__(self, key, value):
        self.children[key] = value

    def __contains__(self, value):
        return value in self.children
