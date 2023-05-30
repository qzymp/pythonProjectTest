import json
filename = 'numbers.json'
with open(filename, encoding='utf-8') as f_obj:
    numbers = json.load(f_obj)

print(numbers)
