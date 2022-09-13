# 字典：键值对

# 创建字典
score = {'jack': 90, 'rose': 99, 'tom': 59}
print('score:', score)

# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
print('items1: ', items1)

# 通过 zip 函数将2个列表压成字典
items2 = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print('items2: ', items2)

# 创建字典的推导式语法
items3 = {num : num ** 2 for num in range(1, 10)}
print('items3: ', items3)

# 对字典中的键值对进行遍历
for key in score:
    print(f'{key}: {score[key]}')

# 更新字典中的元素
score['jack'] = 100
score['qzymp'] = 999
print(f'score: {score}')

