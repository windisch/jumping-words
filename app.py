import tkinter as tk
from text import Text


class WordShuffle():
    def __init__(self, text, seed=42):

        self.text = Text(text)

        self.root = tk.Tk()
        self.label = tk.Label(
            text=self.text.get_string(),
            font=('Nimbus Mono L', 20),
        )
        self.label.pack()
        self.update()

    def start(self):
        self.root.mainloop()

    def update(self):

        self.text.shuffle()

        self.label.configure(text=self.text.get_string())
        self.root.after(100, self.update)


if __name__ == '__main__':

    with open('./example_wiki.txt', 'r') as fh:
        text = "".join(fh.readlines())

    app = WordShuffle(text)
    app.start()
