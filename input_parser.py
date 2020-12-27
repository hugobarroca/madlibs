import requests

class InputParser:
    def __init__(self):
        self.phrases = []
        self.words_to_replace = []
        self.number_of_blanks = 0

    def get_input(self):
        user_input = input("Enter 1 to get a randomly generated phrase from the API, or 2 to enter a phrase yourself:\n")
        if user_input == "1":
            self.get_input_from_the_api()
        else:
            self.get_phrase_with_blanks()
            self.get_words_to_replace()

    def get_input_from_the_api(self):
        response = requests.get("http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=13").json()
        print(response)
        list_of_phrases = response["value"]
        list_of_blanks = response["blanks"]
        nr_phrases = len(list_of_phrases)
        nr_blanks = len(list_of_blanks)
        if nr_phrases == nr_blanks:

    def get_phrase_with_blanks(self):
        while not self.input_is_valid():
            phrase_with_blanks = input('Please write a phrase with underscores to represent blanks:\n')
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








