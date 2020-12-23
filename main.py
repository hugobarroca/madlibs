from blanks_processor import BlanksProcessor
from input_parser import InputParser

if __name__ == '__main__':
    ip = InputParser()
    bp = BlanksProcessor(ip.phrase_with_blanks, ip.words_to_replace)
    print(bp.get_filled_string())


