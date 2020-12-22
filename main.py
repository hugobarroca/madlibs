from blanks_processor import BlanksProcessor

if __name__ == '__main__':
    while True:
        user_input = input('Please write a phrase with underscores to represent blanks:\n')
        if user_input == "q":
            break
        number_of_blanks = user_input.count("_")
        list_of_arguments = []
        for x in range(0, number_of_blanks):
            new_argument = input("Please input word to replace:\n")
            list_of_arguments.append(new_argument)
        bp = BlanksProcessor(user_input)
        print(bp.get_filled_string(list_of_arguments))

