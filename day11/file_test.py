# def main():
#     f = open('a.txt', 'r', encoding='utf-8')
#     print(f.read())
#     print(type(f))
#     f.close()

# def main():
#     try:
#         f = open('b.txt', 'r', encoding='utf-8')
#         print(f.read())
#
#     except FileNotFoundError:
#         print('无法打开指定文件')
#     except LookupError:
#         print('指定了未知的编码')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误')
#     finally:
#         f.close()

# def main():
#     try:
#         with open('a.txt', 'r', encoding='utf-8') as f:
#             # print(f.read())
#             for line in f:
#                 print(type(line))
#                 print(line, end='')
#     except FileNotFoundError:
#         print('文件未找到')

def main():
    with open('a.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(lines)
        list = []
        for line in lines:
            line.rstrip('\n')
            list.append(line)
        print(list)
        # list = [line.rstrip('\n') for line in lines]
        # print(list)

if __name__ == '__main__':
    main()