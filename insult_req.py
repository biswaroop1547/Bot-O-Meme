import requests
import json


def get_insult():

    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

    r = requests.get(url, headers={"Content-type": "application/json"})

    json_form = json.loads(r.text)
    insult = json_form["insult"]

    return insult 