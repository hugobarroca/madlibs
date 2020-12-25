import requests
import pandas as pd
from blanks_processor import BlanksProcessor
from input_parser import InputParser

if __name__ == '__main__':
    response = requests.get("http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=25").json()
    print(response)
    ip = InputParser()
    ip.get_input()
    bp = BlanksProcessor(ip.phrase_with_blanks, ip.words_to_replace)
    print(bp.get_filled_string())


