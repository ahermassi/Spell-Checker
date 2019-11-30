from src.node.TrieNode import TrieNode


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def __contains__(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for c in word:
            if c not in root:  # This is equivalent to: if c not in root.children. See __contains__ method of TrieNode.
                return False
            root = root[c]  # This is equivalent to: root = root.children[c]. See __getitem__ method of TrieNode.
        return root.end_of_word

    def __len__(self):

        def helper(root):
            nonlocal length
            if root.end_of_word:
                length += 1
            else:
                for node in root.children.values():
                    helper(node)

        root, length = self.root, 0
        if not root:
            return 0
        helper(root)
        return length

    def add(self, word):
        """
        Traverse the trie and add new nodes as we go.
        :type word: str
        :rtype: None
        """
        word = word.strip()
        root = self.root  # n is for "node"
        for c in word:
            if c not in root:
                root[c] = TrieNode()
            root = root[c]
        root.end_of_word = True

    def starts_with(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for c in prefix:
            if c not in root:
                return False
            root = root[c]
        return True

