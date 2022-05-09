nameList = ['张三', '李四', '王五']

# length = len(nameList)  # 获取列表长度
# for i in range(0, length):
#     print(nameList[i])

# for name in nameList:
#     print(name)

# 冒泡排序
nums = [5, 1, 7, 6, 8, 2, 4, 3]
for i in range(0, len(nums) - 1):
    for j in range(0, len(nums) - 1- i):
        if nums[j] > nums[j + 1]:
            a = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = a
print(nums)


names=['zhangsan','lisi','chris','jerry','henry']
name = 'zhangsan'
if name in names:
    print('该姓名已存在')
else:
    names.append(name)
print(names)
