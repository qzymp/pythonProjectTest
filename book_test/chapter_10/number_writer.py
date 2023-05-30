import json

numbers = [2, 3, 5, 7, 9, 11]
filename = 'numbers.json'
with open(filename, 'w', encoding='utf-8') as f_obj:
    json.dump(numbers, f_obj)
