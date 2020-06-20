
import requests
import json
import os

DICT_APP_ID = os.environ['DICT_APP_ID']
DICT_APP_KEY = os.environ['DICT_APP_KEY']

def get_meanings(word):
    app_id = DICT_APP_ID
    app_key = DICT_APP_KEY
    language = "en-gb"
    endpoint = "entries"
    word_id = word
    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
    json_form = json.loads(r.text)

    categories = json_form["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]

    definitions = []

    try:
        for d in categories:
            definitions += d["definitions"]

    except KeyError:
        definitions = ["Sorry no definitions found."]
    

    return definitions

# print('\n\n'.join(get_meanings("name")))