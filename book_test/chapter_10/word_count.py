
def count_words(filename):
    """计算一个文件大概包含多少个单词"""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        pass
    else:
        words = contents.strip()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

