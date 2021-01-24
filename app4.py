import json
data = json.load(open("data.json"))
from difflib import get_close_matches

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
    else:
        return "The word does not exist. Please double check it."

word = input("Enter word: ")

print(translate(word))
