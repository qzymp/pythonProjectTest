

# 使用json实现序列化
import json

file = open('names.txt', 'w')
names = ['zhangsan', 'lisi', 'wangwu', 'jerry', 'henry', 'merry', 'chris']

# file.write(names)

# 调用json的dumps方法
# result = json.dumps(names)
# print(result)
# file.write(result)


# json的dump方法
json.dump(names,file)


file.close()

