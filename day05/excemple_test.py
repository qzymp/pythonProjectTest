# 水仙花数：数字每个位上数字的立方之和正好等于它本身
import random

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if low ** 3 + mid ** 3 + high ** 3 == num:
        print(num)

print('------------------------')

# 整数反转
num = 123456789
str = str(num)
print(str)
print(len(str))
# print(str[len(str)-1])
new_str = ''
for i in range(1, len(str) + 1):
    new_str += str[len(str)-i]
print(new_str)


# print(100//3)
# 百钱白鸡：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只
for x in range(0, 100//5):
    for y in range(0, 100//3):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print(f'公鸡：{x}只，母鸡：{y}只，小鸡：{z}只')

print()


money = 10000
while money > 0:
    # 还有钱，可以继续
    while True:
        print(f'还有{money}')
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    first = random.randint(1,6) + random.randint(1, 6)
    if first == 7 or first == 11:
        print('玩家胜')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜')
        money -= debt
    else:
        while True:
            num = random.randint(1,6) + random.randint(1, 6)
            if num == 7:
                print('庄家胜')
                money -= debt
                break
            elif num == first:
                print('玩家胜')
                money += debt
                break

print('你破产里，游戏结束！')

