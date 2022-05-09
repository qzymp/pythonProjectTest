import random

# 定义3个办公室
offices = [[], [], []]
# 定义8位老师
names = ['A','B','C','D','E','F','G','H']

# 把老师随机分配到办公室
for name in names:
    # 获得随机办公室id
    i = random.randint(0, 2)
    # 把老师分配到随机获得的办公室内
    offices[i].append(name)

officeId = 1
for office in offices:
    print(f'办公室{officeId}的人数为{len(office)}')
    i += 1
    for name in office:
        print(name, end='')

    print()




