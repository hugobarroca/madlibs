import requests
import sys


# This class queries the user for input, and processes it in such a way that it ends up storing a list of phrases, and a
# list of words to fill in between those phrases.

class InputParser:
    def __init__(self):
        self.phrases = []
        self.words_to_replace = []

    def get_input(self):
        user_input = input("Enter 1 to enter a phrase yourself, or 2 to get a randomly generated phrase from the API."
                           " Enter \"q\" to quit:\n")
        if user_input == "1":
            self.get_input_from_the_user()
        elif user_input == "2":
            self.get_input_from_the_api()
        elif user_input == "q":
            sys.exit()
        else:
            print("Unrecognized input. Quiting...")
            sys.exit()

    def get_input_from_the_user(self):
        self.fill_list_of_phrases()
        self.fill_words_to_replace()

    def fill_list_of_phrases(self):
        phrase_with_underscores = ''
        while phrase_with_underscores == '':
            phrase_with_underscores = input('Please write a phrase with underscores to represent blanks:\n')
        self.phrases = phrase_with_underscores.split('_')

    def fill_words_to_replace(self):
        self.words_to_replace = []
        number_of_blanks = len(self.phrases) - 1
        for x in range(0, number_of_blanks):
            new_word = input("Please input word to replace:\n")
            self.words_to_replace.append(new_word)

    def get_input_from_the_api(self):
        response = requests.get("http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=13").json()
        self.phrases = response["value"]
        self.phrases.pop()
        blanks = response["blanks"]
        self.fill_words_to_replace_api(blanks)

    def fill_words_to_replace_api(self, blanks):
        self.words_to_replace = []
        for phrase in blanks:
            word = input(f"Please enter a {phrase}:\n")
            self.words_to_replace.append(word)

