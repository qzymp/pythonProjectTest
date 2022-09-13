"""
集合：不会有重复的元素
"""
set1 = {1, 2, 3, 3, 2, 1}
print(set1)
print(len(set1))

set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2,set3)
print(set3)

# 向集合中添加元素
set1.add(4)
set1.add(5)
print(set1)

print('set2', set2)
set2.update([11,22])
print(set2)
# set2.discard(5)
set2.remove(5)
print(set2)
