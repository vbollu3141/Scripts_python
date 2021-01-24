import json
data = json.load(open("data.json"))
from difflib import get_close_matches

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
    else:
        return "The word does not exist. Please double check it."

word = input("Enter word: ")

print(translate(word))
