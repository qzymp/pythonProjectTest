ticket = 0  # 1 有车票  0 没有车票
knife_length = 19    # 刀子长度，单位cm

if ticket == 1:
    print('有车票，可以进站')
    if knife_length < 10:
        print('通过安检')
    else:
        print('没有通过安检')
        print('刀子长度超过规定')
else:
    print('没有车票，不能进站')

print()

money = int(input('公交卡当前余额：'))
has_seat = False
if money >= 2:
    print('公交卡余额足够，可以上车')
    if has_seat:
        print('有空位，可以坐下')
    else:
        print('没有空位，不能坐下')
else:
    print('公交卡余额不足，不能上车')