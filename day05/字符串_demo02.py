str = '今天天气好晴朗，处处好风光呀好风光'

# 获取长度：len
print(len(str))

# 查找指定内容或字符串：find
print(str.find('好风光'))  # '好风光'第一次出现时，'好'的位置
print(str.find('你好'))  # '你好'不存在，返回：-1
print(str.find('风', 12))  # 从下标12开始找'风'
print(str.find('风', 1, 10))  # 从下标1开始到下标10

# rfind()：从右边开始查找
print(str.rfind('好'))

# startswith：判断字符串是否以指定内容开始
print(str.startswith('今'))
print(str.startswith('今日'))

# endswith：判断字符串是否以指定内容结束
print(str.endswith('风光'))
print(str.endswith('风景'))

print()

# isalpha：判断字符串是否纯字母
str = 'hello'
print(str.isalpha())
str = 'hello world'
print(str.isalpha())

print()

# isdigit：判断一个字符串是否是纯数字
str = '1234'
print(str.isdigit())
str = '12.34'
print(str.isdigit())
str = '-123'
print(str.isdigit())

print()

# isalnum: 判断是否由数字和字母组成
str = 'abcd'
print(str.isalnum())
str = '1234'
print(str.isalnum())
str = 'abcd1234'
print(str.isalnum())
str = 'abc1234_'
print(str.isalnum())

print()

# isspace: 判断字符串中是否只包含空格
str = ''
print(str.isspace())
str = '  '
print(str.isspace())
str = '  d'
print(str.isspace())

print()

# count: 计算字符串出现的次数
str = '今天天气好晴朗，处处好风光呀好风光'
print(str.count('风'))

print()

# replace: 替换
newstr = str.replace('好', '坏')
print(str)
print(newstr)
newstr = newstr.replace('坏', '好', 2)
print(newstr)

print()

# 分隔
# split: 以指定字符串为分隔符切片
s = '今天天气好晴朗，处处好风光呀好风光'
result = s.split()
print(result)  # 没有指定分隔符，默认使用空格

result = s.split('好')  # 以‘好’为分隔符
print(result)

result = s.split('好', 2)  # 以‘好’为分隔符，最多切割成3份
print(result)

print()

# rsplit: 从右向左分隔
s = '今天天气好晴朗，处处好风光呀好风光'
result = s.rsplit('好', 1)
print(result)

print()

# splitlines: 按照行分隔，返回一个包含各行作为元素的列表
s = 'hello \nworld'
print(s.splitlines())

# 修改大小写
# capitalize: 每一个单词首字母大写
s = 'hello world'
print(s.capitalize())

# title: 每个单词首字母大写
print(s.title())

# lower: 所有都变成小写
print(s.lower())

# upper: 所有都变成大写
print(s.upper())

print()

# 字符串拼接
# s.join(iterable)  把参数进行遍历，取出参数里的每一项，然后在后面加上mystr
mystr = 'a '
print(mystr.join('hello'))
print(mystr.join(['hi', 'hello', 'good']))

txt = '_'
print(txt.join(['hi', 'hello', 'good']))
print(txt.join(('good', 'hi', 'hello')))
