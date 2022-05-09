nameList = ['张三', '李四', '王五']

# append 把新元素添加到列表末尾
print(nameList)

nameList.append('张三')
print(nameList)

# insert  在指定位置插入元素
nameList.insert(1, '钱七')
print(nameList)

# extend  将另一个集合中的元素添加到列表中
a = ['a', 'b', 'c']
b = ['1', '2', '3']
a.extend(b)
print(a)
print(b)

# 修改元素
nameList = ['张三', '李四', '王五']
nameList[0] = '刘备'
print(nameList)

# 查找元素
nameList = ['张三', '李四', '王五']
result = '张三' in nameList
print(result)

# 删除元素
'''
    del 根据下标删除
    pop 删除最后一个元素
    remove 根据元素的值进行删除    
'''
movieName = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']
print(movieName)
# del movieName[2]
# print(movieName)

# movieName.pop()
# print(movieName)

movieName.remove('指环王')
print(movieName)

'''
排序:sort
'''
a = [1, 342, 353, 21, 5555]
print(a)
a.sort()
print(a)

a.sort(reverse=True)
print(a)

# 请删除列表 words = ['hello','',','good','hi','','yes','','no'] 里所有的空字符串。
words = ['hello', '', ',', 'good', 'hi', '', 'yes', '', 'no']
print(words)
words.remove('')
print(words)
