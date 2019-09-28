import numpy as np
from functools import reduce


class Token(object):
    """
    A single token, like a word.

    Args:
        token (string): The input token
    """
    special_chars = [',', '.', '!', '"', ':']

    def __init__(self, token):
        self.letters = np.fromiter(token, dtype='<U1')

        self.length = self.letters.shape[0]
        if self.letters[-1] in self.special_chars:
            self.length = self.length - 1
        self.idx = np.arange

    def shuffle(self):
        """
        Swaps to randomly selected subsequent letters in the token
        """

        if self.length <= 3:
            return

        i = np.random.randint(1, self.length-2)

        self.letters[i], self.letters[i+1] = self.letters[i+1], self.letters[i]

    def get_string(self):
        """
        Concatenate the letters in the current order and returns them as string.

        Returns:
            string: A concatenation of the current order of the letters
        """
        return reduce(lambda x, y: "{}{}".format(x, y), self.letters)


class Sentence(object):
    """
    A sequence of tokens.

    Args:
        sentence (string): A

    """

    def __init__(self, sentence):

        words = sentence.split(" ")
        self.tokens = [Token(word) for word in words if len(word) > 0]
        self.length = len(self.tokens)

    def shuffle(self, n=2):
        """
        Shuffles randomly selected tokens
        """
        if self.length == 0:
            return

        idx_tokens = np.random.randint(0, self.length, n)
        for idx in idx_tokens:
            self.tokens[idx].shuffle()

    def get_string(self):
        if self.length == 0:
            return " "
        return " ".join([token.get_string() for token in self.tokens])


class Text(object):
    """
    Sequence of sentences.

    Args:
        text (string): A text.
    """

    def __init__(self, text):
        sentences = text.split("\n")
        self.sentenes = [Sentence(s) for s in sentences]
        self.lenght = len(self.sentenes)

    def shuffle(self, n=2):
        for i in range(self.lenght):
            self.sentenes[i].shuffle(n=n)

    def get_string(self):
        return "\n".join([s.get_string() for s in self.sentenes])
