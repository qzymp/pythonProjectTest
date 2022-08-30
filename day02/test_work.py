
'''
华氏摄氏度 转换为摄氏温度
'''
# 华氏摄氏度
f = 28
# 摄氏温度
c = (f - 32) / 1.8

print(f'{f}华氏度 = {c}摄氏度')
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

print()

# 计算圆的面积和周长
r = 1
# 周长
perimeter = 2 * 3.1416 * r
# 面积
area = 3.1416 * (r ** 2)

print(f'周长：{perimeter}, 面积：{area}')
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)

print()

# 判断年份是否为闰年
year = 2004
if year % 4 == 0 and year % 100 != 0:
    print(f'{year}是闰年')
else:
    print(f'{year}不是闰年')





