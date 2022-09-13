"""求最大公约数"""


def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    # if x > y:
    #     x, y = y, x
    # print(x, y)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i

print(gcd(36, 6))


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        print(total)
        temp = temp // 10
    return total == num


print(is_palindrome(123321))

