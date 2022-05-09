# 阶乘
# 循环实现

def cal(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


# print(cal(4))


# 递归实现
def factorial(num):
    result = 1
    if num == 1:
        return 1

    result = num * factorial(num - 1)
    return result


# print(factorial(4))


def test(num):
    if num < 2:
        return num

    return test(num - 1) + test(num - 2)


for i in range(1, 51):
    print(test(i))



