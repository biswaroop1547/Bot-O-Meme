
import requests
import json

def get_meanings(word):
    app_id = "84c0eb6b "
    app_key = "09a6a7a32ef4d5853e699301786c8548"
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