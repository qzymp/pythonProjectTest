sum = 0

for i in range(101):
    sum += i

print(sum)

print('--------------')


for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i} * {j} = {i * j} ',end='')
    print()

print('======================')


for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end='')
    print()


print('---------------------------')

for i in range(1, 6):

    print(' '*(6-1-i) + '*'*i,end='')
    print()


