# 遍历字典的key
dict = {'name': 'zhangsan', 'sex': 'm'}

for key in dict.keys():
        print(key)


# 遍历字典的value
for value in dict.values():
        print(value)

# 遍历字典的项
for item in dict.items():
        print(item)

# 遍历字典的key-value
for key,value in dict.items():
        print(f'{key}={value}')

print('*' * 20)

persons = [{'name': 'zhangsan', 'age': 18},
           {'name': 'lisi', 'age': 20},
           {'name': 'wangwu', 'age': 19},
           {'name': 'jerry', 'age': 21}]


# name = input('请输入姓名：')
# for person in persons:
#         if name == person['name']:
#                 print('用户名已存在，添加失败')
#                 break
#         else:
#                 age = int(input('请输入年龄：'))
#                 newPerson = {'name': name, 'age': age}
#                 persons.append(newPerson)
#                 break
#
# for person in persons:
#         print(person)


dict1 = {"a": 100, "b": 200, "c": 300}
dict2 = {v: k for k, v in dict1.items()}
print(dict2)





