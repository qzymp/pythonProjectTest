# salary = 8000
# days = 5
# def money(salary, days):
#     day_salary = salary / 21.75
#     money = day_salary * (days + 21.75)
#     return money
#
# print(money(salary, days))



# print(15*9500/10000 + 4*15000/10000)
#
# a = 422+96+97+97+423+97+96+97+97
# b = 198+199+200+199+199+200+199+201
# sum = a + b
# print(a / sum)
# print(b / sum)
#
# c = 178266 / 1000 / 60
# print(c)
# 2:56

"""

1.0
1.30
2.0
2.30
3.0
3.
4
4
5
5
6
6
7
7
8
8
9
9
"""


a = 45
res = 1
for i in range(1, 10):
    a = a * 0.025 + a
    print(i)
    print(a)
print(a)

print(a + a * 0.2)
print(45 * 1.375 + (45*1.375*0.2))

# m = 14
# s = 26
# print((m * 60) + s)

# str = '29+1+1073807575+1+21+1+532+175+51+909,29+1+1073807576+0+21+1+532+175+34+1043,29+1+1073807577+2+21+1+532+175+45+907,29+1+1073807658+1+21+1+532+208+49+2315,29+1+1073807659+0+21+1+532+208+39+2309,29+1+1073807660+2+21+1+532+208+48+2303,29+2+1073807963+1+21+1+532+361+53+1645,29+2+1073807964+0+21+1+532+361+28+0,29+2+1073807965+2+21+1+532+361+52+2047,29+2+1073808047+1+21+1+532+391+53+1244,29+2+1073808048+0+21+1+532+391+67+2508,29+2+1073808049+2+21+1+532+391+78+2928,30+1+1073808440+1+21+1+532+511+54+0,30+1+1073808441+0+21+1+532+511+62+883,30+1+1073808442+2+21+1+532+511+55+0,30+1+1073808509+1+21+1+532+541+72+903,30+1+1073808510+0+21+1+532+541+39+3084,30+1+1073808511+2+21+1+532+541+88+908,30+1+1073808546+0+21+1+532+551+48+0,30+1+1073808583+1+21+1+532+571+65+2764,30+1+1073808584+0+21+1+532+571+31+0,30+1+1073808585+2+21+1+532+571+66+3682,30+2+1073808946+1+21+1+532+691+55+0,30+2+1073808947+0+21+1+532+691+46+0,30+2+1073808948+2+21+1+532+691+55+0,30+2+1073808972+1+21+1+532+721+68+0,30+2+1073808973+0+21+1+532+721+56+2010,30+2+1073808974+2+21+1+532+721+78+0,30+2+1073808997+1+21+1+532+727+66+0,30+2+1073809068+1+21+1+532+751+45+0,30+2+1073809069+0+21+1+532+751+34+0,30+2+1073809070+2+21+1+532+751+50+0|67676470772843+-4196+-8284+150216+77398129247339+7514+23600+1+77398129247339,67676470772843+10533+11784+266706+77398129247339+7514+2858+1+77398129247339|2|0|0|0|0||50100+0+0+0+0+0,50110+21+0+0+21+20,50120+0+0+0+7+7,0+0+0+0+0+0,0+0+0+0+0+0'
# list = str.split(',')
# # print(list)
# for val in list:
#     # print(val)
#     list_1 = val.split('+')
#     for i in list_1:
#         print(i + '  ', end='')
#
#     print()



# samsung SM-G9650|7|12|2|7|522|1|77|1|1|1|1105
# samsung SM-G9650|7|12|3|5|142|1|14|0|0|0|508
# samsung SM-G9650|7|12|4|5|154|1|44|0|0|0|507
# samsung SM-G9650|7|12|5|7|173|1|14|0|0|0|497
# samsung SM-G9650|7|12|6|1|545|1|71|0|0|0|496
# samsung SM-G9650|7|12|7|1|127|0|31|0|0|0|394
# samsung SM-G9650|7|12|8|1|174|0|14|0|0|0|397
# samsung SM-G9650|7|12|9|7|132|0|13|0|0|0|397
# samsung SM-G9650|7|12|10|7|184|0|7|0|0|0|407
# samsung SM-G9650|7|12|11|5|166|1|6|0|0|0|535
