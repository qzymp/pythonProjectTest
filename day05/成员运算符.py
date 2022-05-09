msg = 'hello'
char = input('请输入一个字符：')

# 使用字符串的 find 方法可以判断字符是否存在
if msg.find(char) != -1:
    print('您输入的字符存在')
else:
    print('您输入的字符不存在')

# 使用 in 运算符可以查看字符是否存在
if char in msg:
    print('您输入的字符存在')
else:
    print('您输入的字符不存在')
