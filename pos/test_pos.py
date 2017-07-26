# -*- coding: utf-8 -*-
"""
test_pos
----------------------------------
Tests for `pos` module.
"""

import unittest
from config import STANFORD_TAGGER_NAME
from config import NLTK_TAGGER_NAME
from nltk.tokenize import word_tokenize

from POS_tagger import POS_tagger


class TestPOS_tagger(unittest.TestCase):
    """Test suite for the POS_tagger class."""

    def setUp(self):
        self.sentence_1 = "Hola esto es una prueba"
        self.sentence_2 = "Me llamo Juan y soy fuerte y rápido."
        self.sentence_3 = "Mis amigos viven en la playa y van de vacaciones a la montaña"

    def tearDown(self):
        pass

    # STANFORD POS TAGGER TESTS
    # Sentence 1 -> "Hola esto es una prueba"
    # Verbs
    def test_verbs_sentence_1_stanford(self):
        """
        Test function to test the verbs identification in sentence_1
        """
        pos_tagger = POS_tagger(STANFORD_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_1))
        returned_tags = pos_tagger.detect_verbs(all_tags)
        expected_tags = [u'es']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Nouns
    def test_nouns_sentence_1_stanford(self):
        """
        Test function to test the nouns identification in sentence_1
        """
        pos_tagger = POS_tagger(STANFORD_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_1))
        returned_tags = pos_tagger.detect_nouns(all_tags)
        expected_tags = [u'prueba']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Adjectives
    def test_adjectives_sentence_1_stanford(self):
        """
        Test function to test the adjectives identification in sentence_1
        """
        pos_tagger = POS_tagger(STANFORD_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_1))
        returned_tags = pos_tagger.detect_adjectives(all_tags)
        expected_tags = []
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Sentence 2 -> "Me llamo Juan y soy fuerte y rápido."
    # Verbs
    def test_verbs_sentence_2_stanford(self):
        """
        Test function to test the verbs identification in sentence_2
        """
        pos_tagger = POS_tagger(STANFORD_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_2))
        returned_tags = pos_tagger.detect_verbs(all_tags)
        expected_tags = [u'soy', u'llamo']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Nouns
    def test_nouns_sentence_2_stanford(self):
        """
        Test function to test the nouns identification in sentence_2
        """
        pos_tagger = POS_tagger(STANFORD_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_2))
        returned_tags = pos_tagger.detect_nouns(all_tags)
        expected_tags = [u'Juan']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Adjectives
    def test_adjectives_sentence_2_stanford(self):
        """
        Test function to test the adjectives identification in sentence_2
        """
        pos_tagger = POS_tagger(STANFORD_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_2))
        returned_tags = pos_tagger.detect_adjectives(all_tags)
        expected_tags = [u'fuerte', u'rápido']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Sentence 3 -> "Mis amigos viven en la playa y van de vacaciones a la montaña"
    # Verbs
    def test_verbs_sentence_3_stanford(self):
        """
        Test function to test the verbs identification in sentence_3
        """
        pos_tagger = POS_tagger(STANFORD_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_3))
        returned_tags = pos_tagger.detect_verbs(all_tags)
        expected_tags = [u'viven', u'van']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Nouns
    def test_nouns_sentence_3_stanford(self):
        """
        Test function to test the nouns identification in sentence_3
        """
        pos_tagger = POS_tagger(STANFORD_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_3))
        returned_tags = pos_tagger.detect_nouns(all_tags)
        expected_tags = [u'amigos', u'playa', u'vacaciones', u'montaña']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Adjectives
    def test_adjectives_sentence_3_stanford(self):
        """
        Test function to test the adjectives identification in sentence_3
        """
        pos_tagger = POS_tagger(STANFORD_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_3))
        returned_tags = pos_tagger.detect_adjectives(all_tags)
        expected_tags = []
        self.assertEqual(set(returned_tags), set(expected_tags))

    # NLTK POS TAGGER TESTS
    # Sentence 1 -> "Hola esto es una prueba"
    # Verbs
    def test_verbs_sentence_1_nltk(self):
        """
        Test function to test the verbs identification in sentence_1
        """
        pos_tagger = POS_tagger(NLTK_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_1))
        returned_tags = pos_tagger.detect_verbs(all_tags)
        expected_tags = [u'es']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Nouns
    def test_nouns_sentence_1_nltk(self):
        """
        Test function to test the nouns identification in sentence_1
        """
        pos_tagger = POS_tagger(NLTK_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_1))
        returned_tags = pos_tagger.detect_nouns(all_tags)
        expected_tags = [u'prueba']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Adjectives
    def test_adjectives_sentence_1_nltk(self):
        """
        Test function to test the adjectives identification in sentence_1
        """
        pos_tagger = POS_tagger(NLTK_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_1))
        returned_tags = pos_tagger.detect_adjectives(all_tags)
        expected_tags = []
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Sentence 2 -> "Me llamo Juan y soy fuerte y rápido."
    # Verbs
    def test_verbs_sentence_2_nltk(self):
        """
        Test function to test the verbs identification in sentence_2
        """
        pos_tagger = POS_tagger(NLTK_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_2))
        returned_tags = pos_tagger.detect_verbs(all_tags)
        expected_tags = [u'soy', u'llamo']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Nouns
    def test_nouns_sentence_2_nltk(self):
        """
        Test function to test the nouns identification in sentence_2
        """
        pos_tagger = POS_tagger(NLTK_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_2))
        returned_tags = pos_tagger.detect_nouns(all_tags)
        expected_tags = [u'Juan']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Adjectives
    def test_adjectives_sentence_2_nltk(self):
        """
        Test function to test the adjectives identification in sentence_2
        """
        pos_tagger = POS_tagger(NLTK_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_2))
        returned_tags = pos_tagger.detect_adjectives(all_tags)
        expected_tags = [u'fuerte', u'rápido']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Sentence 3 -> "Mis amigos viven en la playa y van de vacaciones a la montaña"
    # Verbs
    def test_verbs_sentence_3_nltk(self):
        """
        Test function to test the verbs identification in sentence_3
        """
        pos_tagger = POS_tagger(NLTK_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_3))
        returned_tags = pos_tagger.detect_verbs(all_tags)
        expected_tags = [u'viven', u'van']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Nouns
    def test_nouns_sentence_3_nltk(self):
        """
        Test function to test the nouns identification in sentence_3
        """
        pos_tagger = POS_tagger(NLTK_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_3))
        returned_tags = pos_tagger.detect_nouns(all_tags)
        expected_tags = [u'amigos', u'playa', u'vacaciones', u'montaña']
        self.assertEqual(set(returned_tags), set(expected_tags))

    # Adjectives
    def test_adjectives_sentence_3_nltk(self):
        """
        Test function to test the adjectives identification in sentence_3
        """
        pos_tagger = POS_tagger(NLTK_TAGGER_NAME)
        all_tags = pos_tagger.get_tags(word_tokenize(self.sentence_3))
        returned_tags = pos_tagger.detect_adjectives(all_tags)
        expected_tags = []
        self.assertEqual(set(returned_tags), set(expected_tags))
