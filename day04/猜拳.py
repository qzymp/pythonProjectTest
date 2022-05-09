import random

# 玩家输入出什么
player = int(input('请输入：剪刀（0） 石头（1） 布（2）:'))
# 电脑随机出一个
computer = random.randint(0, 2)


if computer == 0:
    print('电脑：剪刀')
elif computer == 1:
    print('电脑：石头')
else:
    print('电脑：布')

if player == 0 and computer == 2 or player == 1 and computer == 0 or player == 2 and computer == 1:

    print('玩家胜利')
elif player == computer:
    print('平局')
else:
    print('电脑胜利')
