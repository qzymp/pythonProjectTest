with open('pi_digits.txt', encoding='utf-8') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
