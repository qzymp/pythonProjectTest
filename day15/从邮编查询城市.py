

# 打开文件，获取文件内容
import json

code_list = []

try:
    # 打开文件
    file = open('youbian.txt', 'r', encoding='utf-8')
    # 获取所有数据
    while True:
        # 读取文件中的每一行数据
        content = file.readline().strip(',\n')
        # print(content, type(content))
        if not content:
            # 如果读取一行数据为空，结束循环
            break
        # 将读取出来的每一行内容反序列化成列表
        x = json.loads(content)
        # print(x, type(x))
        # 将每一行数据存储到列表中
        code_list.append(x)
except FileNotFoundError:
    print('未找到文件')


# 邮编
i = '110229'
# print(code_list)
for code in code_list:
    if str(code[0]) == i:
        print(code[1])
        break
else:
    print('未找到')




