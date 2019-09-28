from text import (
    Token,
    Sentence,
    Text
)
import unittest
import numpy as np



class TestToken(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        np.random.seed(31)

    def test_get_string(self):
        token = Token("Hallo")
        self.assertEqual(token.get_string(), 'Hallo')

    def test_shuffle_letters(self):

        word = "Allgäu"
        token = Token(word)
        token.shuffle()

        word_shuffled = token.get_string()

        self.assertEqual(len(word_shuffled), len(word))
        self.assertNotEqual(word_shuffled, word)


class TestSentence(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        np.random.seed(31)

    def setUp(self):
        self.sentence = "This is awesome python code"

    def test_get_string(self):
        sentence = Sentence(self.sentence)
        self.assertEqual(sentence.get_string(), self.sentence)

    def test_shuffle(self):
        sentence = Sentence(self.sentence)
        sentence.shuffle()
        self.assertNotEqual(sentence.get_string(), self.sentence)


class TestText(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        np.random.seed(31)

    def setUp(self):
        self.text = "This is awesome python code.\nIt is free of bugs"

    def test_get_string(self):
        text = Text(self.text)
        self.assertEqual(text.get_string(), self.text)
