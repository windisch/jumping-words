import tkinter as tk
import argparse
from text import Text


class WordShuffle(object):
    """

    Args:
        text (string): Text to be parsed. Lines should be enclosed with :code:`\n`
        fontsize (int): Size of the font displayed
        jump_time (int): Time in milliseconds between two shuffles

    """
    def __init__(self, text, fontsize=20, jump_time=100):

        self.fontsize = fontsize
        self.jump_time = jump_time
        self.text = Text(text)

        self.init()

    def start(self):
        self.root.mainloop()

    def init(self):
        self.root = tk.Tk()
        self.label = tk.Label(
            text=self.text.get_string(),
            font=('Nimbus Mono L', self.fontsize),
        )
        self.label.pack()

        self.root.after(2000, self.update)

    def update(self):
        self.text.shuffle()

        self.label.configure(text=self.text.get_string())
        self.root.after(self.jump_time, self.update)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Let words jump around')
    parser.add_argument(
        'filepath',
        metavar='filepath',
        default='./example_text',
        type=str,
        help='Path to file with example text')

    parser.add_argument(
        '--fontsize',
        metavar='N',
        default=None,
        type=int,
        help='Size of the font displayed')

    parser.add_argument(
        '--jump-time',
        metavar='ms',
        default=None,
        type=int,
        help='Time in milliseconds between two shuffles')

    args = parser.parse_args()

    with open(args.filepath, 'r') as fh:
        text = "".join(fh.readlines())

    WordShuffle(text).start()
