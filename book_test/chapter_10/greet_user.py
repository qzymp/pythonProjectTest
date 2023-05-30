import json

filename = 'username.json'
with open(filename, encoding='utf-8') as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
