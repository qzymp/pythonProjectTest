# 已读取的方式打开csv文件
import csv

file = open('test.csv','r')

# 调用csv模块的reader方法，得到一个可迭代对象
reader = csv.reader(file)

# 对结果进行遍历，获取到结果里的每一行数据
for row in reader:
    print(row)

file.close()