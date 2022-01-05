from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    
    def parse(self, file):
        words = []

        for word in file:
            if word.strip() and not word.startswith("#"):
                words.append(word.strip())
        return words