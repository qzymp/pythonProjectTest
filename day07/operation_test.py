s1 = 'hello ' * 3
print(s1)

s2 = 'world'
s1 += s2
print(s1)

print('ll' in s1)

print('good' in s1)

str = 'abc123456'

print(str[2])
print(str[2:5])
print(str[::-1])

print('-------------------')

str1 = 'hello, world!'
# 计算字符串的长度
print(len(str1))
# 获得字符串首字母大写的拷贝
print(str1.capitalize())
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())
# 获得字符串变大写后的拷贝
print(str1.upper())

# 从字符串中查找字符串的位置
print(str1.find('or'))
print(str1.find('shit'))

# 检查字符串是否以指定的字符串为开头
print(str1.startswith('He'))
print(str1.startswith('hel'))

# 检查字符串是否以指定字符串为结尾
print(str1.endswith('!'))

print('================')

str2 = 'askdj'

# 检查字符串是否由数字构成
print(str2.isdigit())
# 检查字符串是否由字母构成
print(str2.isalpha())
# 检查字符串是否由字母和数字构成
print(str2.isalnum())

str3 = '   qzympp@163.com   '
# 删除字符串两侧的空格
print(str3.strip())








