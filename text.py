import numpy as np
from functools import reduce


class Token(object):
    """
    TODO: Deal with special signs
    """
    special_chars = [',', '.', '!']

    def __init__(self, token):
        self.letters = np.fromiter(token, dtype='<U1')

        self.length = self.letters.shape[0]
        if self.letters[-1] in self.special_chars:
            self.length = self.length - 1
        self.idx = np.arange

    def shuffle(self, keep_endpoints=True):

        if self.length == 1:
            return

        if keep_endpoints and self.length <= 3:
            return

        if keep_endpoints:
            i, j = np.random.randint(1, self.length-1, 2)
        else:
            i, j = np.random.randint(0, self.length, 2)

        if i == j:
            return

        l_i = self.letters[i]
        l_j = self.letters[j]
        self.letters[i] = l_j
        self.letters[j] = l_i

    def get_string(self):
        return reduce(lambda x, y: "{}{}".format(x, y), self.letters)


class Line(object):

    def __init__(self, line):

        words = line.split(" ")
        self.tokens = [Token(word) for word in words]
        self.length = len(self.tokens)

    def shuffle(self, n=2):
        """
        Shuffles randomly selected tokens
        """
        idx_tokens = np.random.randint(0, self.length, n)
        for idx in idx_tokens:
            self.tokens[idx].shuffle()

    def get_string(self):
        return " ".join([token.get_string() for token in self.tokens])


class Text(object):

    def __init__(self, text):
        lines = text.split("\n")
        self.lines = [Line(l) for l in lines if len(l) > 0]
        self.lenght = len(self.lines)

    def shuffle(self, n=2):
        for i in range(self.lenght):
            self.lines[i].shuffle(n=n)

    def get_string(self):
        return "\n".join([line.get_string() for line in self.lines])
