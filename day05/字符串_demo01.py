# name = 'abcdef'
# print(name[0])
# print(name[1])

# while 语句遍历
# msg = 'hello world'
# i = 0
# while i < len(msg):
#     print(msg[i])
#     i += 1

# for语句遍历
# msg = 'hello world'
# for i in msg:
#     print(i)

# 切片
s = 'hello world'
print(s)

# 字符串里第4个元素
print(s[4])

print(s[3:7])   # 包含下标3，不包含下标7

print(s[:])     # 取出所有元素,没有起始位结束为之分，默认步长1

print(s[1:])    # 从下标1开始，取出后面所有

print(s[:4])    # 从下标0开始，取出到下标4（不包含下标4）

print(s[:-1])   # 从起始位开始，取出到 倒数第一位元素（不包含结束位）

print(s[-4:-1]) # 从倒数第4位开始，到倒数第一个（不包含结束位）

print(s[1:5:2]) # 从第一位开始，到第5位（不包含第5位），步长2

print(s[7:2:-1])    # 从第7位开始，到第2位（倒着数）

print(s[::-1])  # 从后向前


