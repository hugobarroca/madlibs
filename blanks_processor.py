# This class replaces the underscores on a given string with the appropriate given arguments.
class BlanksProcessor:
    def __init__(self, phrases, words):
        self.phrases = phrases
        self.words = words

    def get_filled_string(self):
        temp_string = ''
        nr_phrases = len(self.phrases)

        for x in range(0, nr_phrases):
            if x != nr_phrases - 1:
                temp_string += self.phrases[x] + self.words[x]
            else:
                temp_string += self.phrases[x]
        return temp_string
