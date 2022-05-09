# 遍历字符串
# s = 'hello'
# for a in s:
#     print(a)

print()

# 打印数字
# for i in range(5):
#     print(i)

# 计算1~100和
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# break  结束整个循环
# i = 0
# while i < 10:
#     i += 1
#     if i == 7:
#         break
#     print(i)

# continue  结束本次循环，继续下次
# i = 1
# while i < 10:
#     i += 1
#     if i == 7:
#         continue
#     print(i)

# 打印 1~100 内，不能被 7 整除的所有数字。
# i = 0
# while i <= 100:
#     i += 1
#     if i % 7 == 0:
#         continue
#     print(i)

# 计算 1~100 内，所有不能被 7 整除的数字之和。
# sum = 0
# i = 0
# while i <= 100:
#     i += 1
#     if i % 7 == 0:
#         continue
#     sum += i
# print(sum)

# 不断的询问用户，"我爱你，你爱我吗?"，只有用户回答"爱"时，结束循环。
# while True:
#     print('"我爱你，你爱我吗?')
#     answer = input()
#     if answer == '爱':
#         break

# break和continue在嵌套循环中使用时，只对最内层循环有效。
i = 0

while i < 10:
    i += 1
    if i == 7:
        continue
    print(f'i = {i}')
    j = 0
    while j < 10:
        print(f'j = {j}')
        j += 1





