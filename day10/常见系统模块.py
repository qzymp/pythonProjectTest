import hashlib
import math
import random
import datetime
import time

print(math.fabs(-100))  # 取绝对值
print(math.ceil(43.1))  # 向上取整

# 生成[10， 30]的随机整数
print(random.randint(10, 30))

# 从列表中随机取出一个元素
print(random.choice('abcdefg'))

# 从列表中随机取出指定个数的元素
print(random.sample('abcdefghi', 3))

# 定义函数，生成指定长度的验证码
def code(length):
    list = random.sample('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789', length)
    code = ''
    for i in list:
        code += i
    return code
code = code(4)
print(code)

print()

# 创建一个日期
print(datetime.date(2022, 5, 5))
# 创建一个时间
print(datetime.time(20, 35, 59))
# 获取当前的日期时间
print(datetime.datetime.now())
# 计算三天后的日期时间
print(datetime.datetime.now() + datetime.timedelta(3))

print()

# 获取从1970-01-01 00：00：00到现在的秒数
print(time.time())
# 按照指定格式输出时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))

print('hello')
# 让线程暂停10s
# print(time.sleep(10))
print('world')

print()

str = '这是一个测试'

# 创建md5对象
hl = hashlib.md5('hello'.encode('utf-8'))
print('MD5加密后为：' + hl.hexdigest())
print(hl)

h1 = hashlib.sha1('123456'.encode())
print(h1.hexdigest())
h2 = hashlib.sha224('123456'.encode())
print(h2.hexdigest())
h3 = hashlib.sha256('123456'.encode())
print(h3.hexdigest())






