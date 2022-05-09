# 使用write向文件中写入数据
# f = open('test.txt','w')
# f.write('hello world, i am here!\n' * 5)
# f.close()

# 使用read读取文件数据
f = open('test.txt', 'r')
content = f.read(5) # 最多读取5个数据
print(content)

print('-' * 30)

content = f.read()  # 从上次读取的位置继续读取剩下的所有数据
print(content)

f.close()

f = open('test.txt', 'r')
content = f.readline()  # 读取一行数据
print(f'1:{content}')

content  = f.readline()
print(f'2:{content}')

f.close()

print('*' * 30)

f = open('test.txt', 'r')
# 读取文件所有数据，每一行数据作为一个元素，返回一个列表
content = f.readlines()
print(type(content))

for temp in content:
    print(temp)

f.close()
