import string
from collections import defaultdict
from src.trie.trie import Trie


def one_edit(word):
    """ Generate all the possible words that are one edit apart from the given word.
        There are 4 possibilities to perform one edit:
        Delete a character
        Swap two adjacent characters
        Replace a character
        Add a character into s to get t
    """
    alphabet = string.ascii_lowercase
    deletes = [word[:i] + word[i + 1:] for i in range(len(word))]
    swaps = [word[:i] + word[i+1] + word[i] + word[i+2:] for i in range(len(word) - 1)]
    replaces = [word[:i] + c + word[i+1:] for i in range(len(word)) for c in alphabet]
    inserts = [word[:i] + c + word[i:] for i in range(len(word) + 1) for c in alphabet]
    return set(deletes + swaps + replaces + inserts)


def two_edits(word):
    """ Generate all the possible words that are two edits apart from the given word. These are equal to the one
        edits of the one edit words.
    """
    return set(w2 for w1 in one_edit(word) for w2 in one_edit(w1))


class SpellChecker:

    def __init__(self, file_name):
        """
        Load the list of words into the trie and construct a frequency map of the words.
        """
        self.dictionary = Trie()
        self.counter = defaultdict(int)
        with open(file_name, 'r') as file:
            for line in file:
                for word in line.split():
                    self.dictionary.add(word.lower())
                    self.counter[word] += 1

    def spell_check(self, word):
        """
        Find the probabilities of possible corrections of the word and return the most probable.
        """
        counter = self.counter
        total = sum(counter.values())
        if not word or word.isdigit():
            return 'No suggestion'
        if self.corrections(word):
            return max(self.corrections(word), key=lambda w: counter[w.lower()] / total)
        return 'No suggestion'

    def corrections(self, word):
        """ Find the possible corrections of the word. """
        return self.valid([word]) or self.valid(one_edit(word)) or self.valid(two_edits(word))

    def valid(self, words):
        """ Filter out the words that do not appear in the trie. """
        return set(w for w in words if w in self.dictionary)

