# -*- coding: utf-8 -*-

import re
import codecs
from config import WORDS_FILE_PATH
from collections import Counter

class Spanish_Spell_Checker(object):
    """Class to check the spelling of a word in Spanish"""
    def __init__(self):
        # To convert the files to utf-8
        # vim +"set nobomb | set fenc=utf8 | x" FILE_NAME.txt
        with codecs.open(WORDS_FILE_PATH, 'r', 'utf-8') as f:
            all_words = f.read()
        # Other encodings we may need to use:
        # all_words = codecs.open(WORDS_FILE_PATH, 'r', 'iso-8859-1').read()
        # all_words = open(WORDS_FILE_PATH).read()
        self.WORDS = Counter(self.words(all_words))

    def words(self, text):
        """Find all the words in the text file."""
        return re.findall(r'\w+', text.lower())

    def P(self, word):
        "Probability of `word`."
        N=sum(self.WORDS.values())
        return self.WORDS[word] / N

    def edits1(self, word):
        "All edits that are one edit away from `word`."
        letters    = 'aábcdeéfghiíjklmnñoópqrstuúüvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word):
        "All edits that are two edits away from `word`."
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

    def known(self, words):
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in self.WORDS)

    def candidates(self, word):
        "Generate possible spelling corrections for word."
        return (self.known([word]) or \
            self.known(self.edits1(word)) or \
            self.known(self.edits2(word)) or \
            [word])

    def correction(self, word):
        "Most probable spelling correction for word."
        return max(self.candidates(word), key=self.P)



if __name__ == '__main__':
    #from spell import Spanish_Spell_Checker
    sp = Spanish_Spell_Checker()
    #print(sp.correction("ohla"))
    print(sp.correction("ohla"))
    print(sp.correction("altz"))
    print(sp.correction("mobil"))
