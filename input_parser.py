# Gets a valid string from the user.
class InputParser:
    def __init__(self):
        self.phrase_with_blanks = ''
        self.words_to_replace = []
        self.number_of_blanks = 0

    def get_input(self):
        self.get_phrase_with_blanks()
        self.get_words_to_replace()

    def get_phrase_with_blanks(self):
        while not self.input_is_valid():
            self.phrase_with_blanks = input('Please write a phrase with underscores to represent blanks:\n')
        self.number_of_blanks = self.phrase_with_blanks.count("_")

    def get_words_to_replace(self):
        for x in range(0, self.number_of_blanks):
            new_word = input("Please input word to replace:\n")
            self.words_to_replace.append(new_word)

    def input_is_valid(self):
        if '_' not in self.phrase_with_blanks:
            return False
        if self.phrase_with_blanks == '':
            return False
        return True








