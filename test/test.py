import unittest
from src.trie.spell_checker import SpellChecker


class TestSpellChecker(unittest.TestCase):

    spell_checker = SpellChecker('../src/words.txt')

    def test_length(self):
        self.assertEqual(len(self.spell_checker.dictionary), 1902)

    def test_spell_checker(self):
        self.assertEqual(self.spell_checker.spell_check('advntres'), 'adventures')
        self.assertEqual(self.spell_checker.spell_check('bttom'), 'bottom')
        self.assertEqual(self.spell_checker.spell_check('othghr'), 'other')
        self.assertEqual(self.spell_checker.spell_check('restriktins'), 'restrictions')
        self.assertEqual(self.spell_checker.spell_check('involwd'), 'involved')
        self.assertEqual(self.spell_checker.spell_check(''), 'No suggestion')
        self.assertEqual(self.spell_checker.spell_check('1337'), 'No suggestion')


if __name__ == '__main__':
    unittest.main()
