from spell_checker import SpellChecker

if __name__ == '__main__':

    print('\nThis is a simple deterministic spell checker. It corrects lower/upper case and mistyped vowels.')
    print('At the prompt, enter the word you want to spell check.\n')

    spell_checker = SpellChecker()

    while True:
        word = input('> ')
        result = spell_checker.spell_check(word.strip().lower())
        if result == 'No suggestion':
            print(result)
        else:
            print('Did you mean \'' + result + '\' ?')
