import numpy as np
from functools import reduce


class Token(object):
    """
    TODO: Deal with special signs
    """
    special_chars = [',', '.', '!', '"', ':']

    def __init__(self, token):
        self.letters = np.fromiter(token, dtype='<U1')

        self.length = self.letters.shape[0]
        if self.letters[-1] in self.special_chars:
            self.length = self.length - 1
        self.idx = np.arange

    def shuffle(self):

        if self.length <= 3:
            return

        i = np.random.randint(1, self.length-2)

        self.letters[i], self.letters[i+1] = self.letters[i+1], self.letters[i]

    def get_string(self):
        return reduce(lambda x, y: "{}{}".format(x, y), self.letters)


class Line(object):

    def __init__(self, line):

        words = line.split(" ")
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

    def __init__(self, text):
        lines = text.split("\n")
        self.lines = [Line(l) for l in lines]
        self.lenght = len(self.lines)

    def shuffle(self, n=2):
        for i in range(self.lenght):
            self.lines[i].shuffle(n=n)

    def get_string(self):
        return "\n".join([line.get_string() for line in self.lines])
