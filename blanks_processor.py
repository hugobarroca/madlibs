class BlanksProcessor:
    def __init__(self, string_with_blanks):
        self.string_with_blanks = string_with_blanks

    def get_filled_string(self, list_of_arguments):
        temp_string = self.string_with_blanks
        for arg in list_of_arguments:
            temp_string = temp_string.replace("_", str(arg), 1)
        return temp_string
