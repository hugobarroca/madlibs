import requests
import json
import pandas as pd
from blanks_processor import BlanksProcessor
from input_parser import InputParser

#Test
def json_print(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


if __name__ == '__main__':
    response = requests.get("http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=25").json()
    json_print(response)

    # ip = InputParser()
    # ip.get_input()
    # bp = BlanksProcessor(ip.phrase_with_blanks, ip.words_to_replace)
    # print(bp.get_filled_string())
