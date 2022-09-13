"""
元组：元组中的元素不可修改
"""
# 定义元组
t = ('张三', 18, True, '广东深圳')
print(t)
# 获取元组中的数据
print(t[1])
# 遍历元组中的元素
for ele in t:
    print(ele)
# 重新给元组赋值
# t[0] = '李四'

t = ('李四', 44, False, 'HENAN')
# 将元组转换成列表
person = list(t)
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)



