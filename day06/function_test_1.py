import random


def fac(num):
    """求阶乘"""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


print(fac(9))

# a = random.randint(1, 6)

# 可变参数
def add(*args):
    total = 0
    for var in args:
        total += var
    return total

print(add(1,2,3,3,4,1))
