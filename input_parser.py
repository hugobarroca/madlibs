# Gets a valid string from the user.
class InputParser:
    def __init__(self):
        self.user_input = ''
        self.number_of_blanks = 0
        self.words_to_replace = []

    def get_input(self):
        self.get_phrase_with_blanks()

        for x in range(0, self.number_of_blanks):
            new_word = input("Please input word to replace:\n")
            self.words_to_replace.append(new_word)

    def get_phrase_with_blanks(self):
        while not self.input_is_valid():
            self.user_input = input('Please write a phrase with underscores to represent blanks:\n')
        self.number_of_blanks = self.user_input.count("_")

    def get_word_list(self):
        pass

    def input_is_valid(self):
        if '_' not in self.user_input:
            return False
        if self.user_input == '':
            return False
        return True








