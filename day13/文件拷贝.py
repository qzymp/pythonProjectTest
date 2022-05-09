# 文件名
file_name = 'test.txt'

# 打开文件
old_file = open(file_name, 'rb')

# 分隔文件名字
file_names = file_name.split('.', maxsplit = 1)

# 新文件名
new_file_name = file_names[0] + '.bak' + file_names[1]

# 创建新文件
new_file = open(new_file_name, 'wb')

# 把旧文件数据写入到新文件中
data = old_file.readlines()
for row in data:
    new_file.write(row)

# 关闭文件
old_file.close()
new_file.close()
