list1 = [1, 3, 5, 7, 100]

print(list1)
# * 表示列表元素重复
list2 = ['hello'] * 3
print(list2)

# 计算列表长度（元素个数）
print(len(list1))

# 下标/索引运算
print(list1[1]) # 3
print(list1[-1]) # 100

list1[2] = 200
print(list1)

# 通过循环用下标遍历列表
for i in range(len(list1)):
    print(list1[i])

# 通过 enumerate 函数处理列表后再遍历
for index, ele in enumerate(list1):
    print(index, ele)

list1 = [1,3,5,7,100]
# 添加元素
list1.append(200)
print(list1)
list1.insert(1,50)
print(list1)
# 合并2个列表
list1 += [1000, 2000]
print(list1)

# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)

print(list1)

# 删除指定位置的元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)

print('--------------------------')

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print(fruits)
# 列表切片
print(fruits[1:4])
# 可以通过完整切片复制列表
fruits2 = fruits[:]
print(fruits2)

# 可以通过反向切片，获得倒转后的列表
print(fruits[::-1])

print('=============================')

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
print(list2)
list3 = sorted(list1,reverse=True)
print(list3)
list4 = sorted(list1, key=len, reverse=True)
print(list4)





