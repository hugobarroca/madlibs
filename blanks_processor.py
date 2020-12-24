# This class replaces the underscores on a given string with the appropriate given arguments.
class BlanksProcessor:
    def __init__(self, string_with_blanks, list_of_arguments):
        self.string_with_blanks = string_with_blanks
        self.list_of_arguments = list_of_arguments

    def get_filled_string(self):
        temp_string = self.string_with_blanks
        for arg in self.list_of_arguments:
            temp_string = temp_string.replace("_", str(arg), 1)
        return temp_string
