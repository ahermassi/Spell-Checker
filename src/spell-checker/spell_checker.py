from trie import Trie


class SpellChecker:

    def __init__(self):
        """
        Load the list of words into the trie.
        """
        self.root = Trie()
        with open('../words.txt', 'r') as file:
            for word in file:
                self.root.add(word)

