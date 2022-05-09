# 转换整数
print(int('123'))  # 123 将字符串转换成整数

print(int(123.456))  # 123 将浮点数转换成整数

print(int(True))  # 1 布尔值True转换成整数 1

print(int(False))  # 0 布尔值False转换成整数 0

# print(int('123.456'))
# print(int('122as'))

# 使用 int() 函数进行类型转换时，可以传入2个参数，第二个参数表示进制
print(int('21', 8))
print(int('F0', 16))

# print(int('19', 8))

print()

# 转换浮点数
print(float('12.34'))

print(float('12'))

# 转换成字符串
str1 = str(12)
str2 = str(12.34)
str3 = str(True)
print(type(str1), type(str2), type(str3))
