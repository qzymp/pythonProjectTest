age = 30
if age >= 18:
    print('我已经成年了')

print()

ticket = 0  #1 有车票  0 没有车票
if ticket == 1:
    print('有车票，可以上车')
else:
    print('没有车票，不能上车')

print()

# 从键盘输入身高，如果身高没有超过150cm，则进动物园不用买票，否则需要买票。
# high = int(input('请输入身高: '))
# if high <= 150:
#     print('进动物园不用买票')
# else:
#     print('需要买票')

score = -15
if score >= 90 and score <= 100:
    print('本次考试，等级为A')
elif score >= 80:
    print('本次考试，等级为B')
elif score >= 70:
    print('本次考试，等级为C')
elif score >= 60:
    print('本次考试，等级为D')
elif score >= 0:
    print('本次考试，等级为E')
else:
    print('请输入正确的成绩')