import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif length(get_close_matches(word,data.keys())) > 0:   
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no:" % get_close_matches(word, data.keys())[0]) 
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "The Word does not exist. Please double check it"
        else:
            return "We did not understand your entry"
    else:        
        return "The Word does not exist. Please double check it"

user_choice = input(" Enter Word ")  
output = translate(user_choice)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)        