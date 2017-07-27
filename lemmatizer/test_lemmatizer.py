# -*- coding: utf-8 -*-
"""
test_lemmatizer
----------------------------------
Tests for `lemmatizer` module.
"""

import unittest

from lemmatizer import Spanish_Lemmatizer


class TestLemmatizer(unittest.TestCase):
    """Test suite for the Spanish_Lemmatizer class."""

    def setUp(self):
        self.lemmatizer = Spanish_Lemmatizer()

    def tearDown(self):
        pass

    # -ar verbs
    # Infinitive
    def test_keyword_hablar(self):
        """
        Test function to test the keyword "hablar"
        """
        returned_lemma = self.lemmatizer.get_lemma("hablar")
        expected_lemma = "hablar"
        self.assertEqual(returned_lemma, expected_lemma)

    # Gerund
    def test_keyword_hablando(self):
        """
        Test function to test the keyword "hablando"
        """
        returned_lemma = self.lemmatizer.get_lemma("hablando")
        expected_lemma = "hablar"
        self.assertEqual(returned_lemma, expected_lemma)

    # One last example for -ar verb
    def test_keyword_hablasemos(self):
        """
        Test function to test the keyword "hablásemos"
        """
        returned_lemma = self.lemmatizer.get_lemma("hablásemos")
        expected_lemma = "hablar"
        self.assertEqual(returned_lemma, expected_lemma)

    # -er verbs
    # Infinitive
    def test_keyword_comer(self):
        """
        Test function to test the keyword "comer"
        """
        returned_lemma = self.lemmatizer.get_lemma("comer")
        expected_lemma = "comer"
        self.assertEqual(returned_lemma, expected_lemma)

    # Gerund
    def test_keyword_comiendo(self):
        """
        Test function to test the keyword "comiendo"
        """
        returned_lemma = self.lemmatizer.get_lemma("comiendo")
        expected_lemma = "comer"
        self.assertEqual(returned_lemma, expected_lemma)

    # One last example for -er verb
    def test_keyword_comieran(self):
        """
        Test function to test the keyword "comieran"
        """
        returned_lemma = self.lemmatizer.get_lemma("comieran")
        expected_lemma = "comer"
        self.assertEqual(returned_lemma, expected_lemma)

    # -ir verbs
    # Infinitive
    def test_keyword_morir(self):
        """
        Test function to test the keyword "morir"
        """
        returned_lemma = self.lemmatizer.get_lemma("morir")
        expected_lemma = "morir"
        self.assertEqual(returned_lemma, expected_lemma)

    # Gerund
    def test_keyword_muriendo(self):
        """
        Test function to test the keyword "muriendo"
        """
        returned_lemma = self.lemmatizer.get_lemma("muriendo")
        expected_lemma = "morir"
        self.assertEqual(returned_lemma, expected_lemma)

    # One last example for -ir verb
    def test_keyword_muriesen(self):
        """
        Test function to test the keyword "muriesen"
        """
        returned_lemma = self.lemmatizer.get_lemma("muriesen")
        expected_lemma = "morir"
        self.assertEqual(returned_lemma, expected_lemma)

    # Some adjectives
    def test_keyword_brillante(self):
        """
        Test function to test the keyword "brillante"
        """
        returned_lemma = self.lemmatizer.get_lemma("brillante")
        expected_lemma = "brillante"
        self.assertEqual(returned_lemma, expected_lemma)

    def test_keyword_alto(self):
        """
        Test function to test the keyword "alto"
        """
        returned_lemma = self.lemmatizer.get_lemma("alto")
        expected_lemma = "alto"
        self.assertEqual(returned_lemma, expected_lemma)

    def test_keyword_azul(self):
        """
        Test function to test the keyword "azul"
        """
        returned_lemma = self.lemmatizer.get_lemma("azul")
        expected_lemma = "azul"
        self.assertEqual(returned_lemma, expected_lemma)

    # Adverbs
    def test_keyword_subitamente(self):
        """
        Test function to test the keyword "súbitamente"
        """
        returned_lemma = self.lemmatizer.get_lemma("súbitamente")
        expected_lemma = "súbitamente"
        self.assertEqual(returned_lemma, expected_lemma)

    def test_keyword_siempre(self):
        """
        Test function to test the keyword "siempre"
        """
        returned_lemma = self.lemmatizer.get_lemma("siempre")
        expected_lemma = "siempre"
        self.assertEqual(returned_lemma, expected_lemma)

    # Nouns
    def test_keyword_nino(self):
        """
        Test function to test the keyword "niño"
        """
        returned_lemma = self.lemmatizer.get_lemma("niño")
        expected_lemma = "niño"
        self.assertEqual(returned_lemma, expected_lemma)

    def test_keyword_nina(self):
        """
        Test function to test the keyword "niña"
        """
        returned_lemma = self.lemmatizer.get_lemma("niña")
        expected_lemma = "niño"
        self.assertEqual(returned_lemma, expected_lemma)

    def test_keyword_ninos(self):
        """
        Test function to test the keyword "niños"
        """
        returned_lemma = self.lemmatizer.get_lemma("niños")
        expected_lemma = "niño"
        self.assertEqual(returned_lemma, expected_lemma)

    def test_keyword_ninas(self):
        """
        Test function to test the keyword "niñas"
        """
        returned_lemma = self.lemmatizer.get_lemma("niñas")
        expected_lemma = "niño"
        self.assertEqual(returned_lemma, expected_lemma)

    # Custom use case that should return the input word
    def test_keyword_jpkl(self):
        """
        Test function to test the keyword "jpkl"
        """
        returned_lemma = self.lemmatizer.get_lemma("jpkl")
        expected_lemma = "jpkl"
        self.assertEqual(returned_lemma, expected_lemma)
