
'''
    集合 set 是无序不重复序列
'''
# set = set(('Google', 'Runoob', 'Taobao'))
# print(set)

# 集合中新增元素
# set.add('Facebook')
# print(set)

# 集合中新增列表、元组、字典
# set.update({'name': 'zhangsan', 'age':18})
# print(set)

# 集合中移除元素
# set.remove('Facebook')
# print(set)

# set.remove('Facebook')

print('-' * 20)

nums=[5,8,7,6,4,1,3,5,1,8,4]
s = set()
s.update(nums)
print(s)
nums2 = list(s)
print(nums2)
nums2.sort(reverse=True)
print(nums2)



