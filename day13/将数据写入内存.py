
# StringIO
# StringIO 可以将字符串写入到内存
# 创建一个StringIO对象
from io import StringIO, BytesIO

f = StringIO()

# 可以向操作文件一样
f.write('hello')
f.write('world')

# 使用文件的read方法,不能读取到数据
print(f.read())

# 使用getvalue，可以读取到
print(f.getvalue())

f.close()

b = BytesIO()

b.write('你好'.encode('utf-8'))
b.write('中国'.encode('utf-8'))

print(b.getvalue())

b.close()