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



'''
       The following are tests using `doctest`. To run the tests do:
           python spellcheck-trie.py -t
       TESTS
       >>> s.spellcheck('sandwich')
       'sandwich'
       >>> s.spellcheck('little')
       'little'
       >>> s.spellcheck('aapple')
       'apple'
       >>> s.spellcheck('sheeeeep')
       'sheep'
       >>> s.spellcheck('peepple')
       'people'
       >>> s.spellcheck('sheeple')
       'NO SUGGESTION'
       >>> s.spellcheck('inSIDE')
       'inside'
       >>> s.spellcheck('jjoobbb')
       'job'
       >>> s.spellcheck('weke')
       'wake'
       >>> s.spellcheck('CUNsperrICY')
       'conspiracy'
       >>> s.spellcheck('ffoaoaoaoaoaoaaoaoaoaoaoadd')
       'food'
       >>> s.spellcheck('FOOD')
       'food'

       PATHOLOGICAL TESTS
       >>> s.spellcheck('')
       'NO SUGGESTION'
       >>> s.spellcheck('1337')
       'NO SUGGESTION'
       >>> s.spellcheck('woot!')
       'NO SUGGESTION'
       >>> s.spellcheck('two words')
       'NO SUGGESTION'
       >>> s.spellcheck(u'ಠ_ಠ')
       'NO SUGGESTION'
       >>> s.spellcheck('fo0bar')
       'NO SUGGESTION'
       '''