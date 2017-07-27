# -*- coding: utf-8 -*-
"""
test_lemmatizer
----------------------------------
Tests for `lemmatizer` module.

# python3 -m unittest discover
"""

import unittest

from spell import Spanish_Spell_Checker


class TestSpell(unittest.TestCase):
    """
    Test suite for the Spanish_Spell_Checker class.
    Based on the code provided by Peter Norvig (http://norvig.com/spell-correct.html)
    """

    def setUp(self):
        self.spell_checker = Spanish_Spell_Checker()

    def tearDown(self):
        pass

    def test_keyword_hablar(self):
        """
        Test function to test the keyword "hablar"
        """
        returned_word = self.spell_checker.correction("hablar")
        expected_word = "hablar"
        self.assertEqual(returned_word, expected_word)

    def test_keyword_habar(self):
        """
        Test function to test the keyword "habar"
        """
        returned_word = self.spell_checker.correction("habar")
        expected_word = "hablar"
        self.assertEqual(returned_word, expected_word)

    def test_keyword_kamon(self):
        """
        Test function to test the keyword "ohla"
        """
        returned_word = self.spell_checker.correction("ohla")
        expected_word = "hola"
        self.assertEqual(returned_word, expected_word)

    def test_keyword_caminata(self):
        """
        Test function to test the keyword "caminata"
        """
        returned_word = self.spell_checker.correction("caas")
        expected_word = "casa"
        self.assertEqual(returned_word, expected_word)

    def test_keyword_llendo(self):
        """
        Test function to test the keyword "llendo"
        """
        returned_word = self.spell_checker.correction("llendo")
        expected_word = "lleno"
        self.assertEqual(returned_word, expected_word)
