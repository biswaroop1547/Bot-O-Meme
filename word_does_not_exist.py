
import requests
from bs4 import BeautifulSoup
import json


def this_word_does_not_exist():

    URL = "https://www.thisworddoesnotexist.com/"

    content = requests.get(URL).content.decode("utf-8")
    soup = BeautifulSoup(content, "html.parser")
    
    text = str(soup("script")[2])
    data_dict = eval(json.loads(json.dumps(text[101:text.index("permalink") - 5].replace("\\", "").replace("null", "None").replace("true", "True").replace("false", "False").replace('"', '\''))))
    
    word = data_dict['word'].capitalize()
    definition = data_dict['definition'].capitalize()
    example = data_dict['example'].capitalize()
    exists = data_dict['probably_exists'] == True

    return {
        'word' : word,
        'definition' : definition,
        'example' : example,
        'exists' : exists
    }



if __name__ == '__main__':
    print(this_word_does_not_exist())