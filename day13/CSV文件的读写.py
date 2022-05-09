

# 以写入的方式打开/创建一个csv文件
import csv

file = open('test.csv', 'w')

# 调用writer方法，传入csv文件对象，得到的结果是一个csvwriter对象
writer = csv.writer(file)

# 调用csvwriter对象的writeow方法，一行行的写入数据
writer.writerow(['name', 'age', 'score'])

# 调用writerows方法，一次写入多行数据
writer.writerows([['zhangsan', '18', '98'],['lisi', '20', '99'], ['wangwu', '17', '90'], ['jerry', '19', '95']])

file.close()


