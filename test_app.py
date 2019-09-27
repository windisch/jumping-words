from text import (
    Token,
    Line,
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


class TestLine(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        np.random.seed(31)

    def setUp(self):
        self.line = "This is awesome python code"

    def test_get_string(self):
        line = Line(self.line)
        self.assertEqual(line.get_string(), self.line)

    def test_shuffle(self):
        line = Line(self.line)
        line.shuffle()
        self.assertNotEqual(line.get_string(), self.line)


class TestText(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        np.random.seed(31)

    def setUp(self):
        self.text = "This is awesome python code.\nIt is free of bugs"

    def test_get_string(self):
        text = Text(self.text)
        self.assertEqual(text.get_string(), self.text)
