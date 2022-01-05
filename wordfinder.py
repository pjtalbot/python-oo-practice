"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):

        file = open(path)

        self.words = self.parse(file)

        print(f"{len(self.words)} words read")

    def parse(self, file):
        return [word.strip() for word in file]

    def random(self):
        return random.choice(self.words)