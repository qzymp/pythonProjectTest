# 定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        return '<b>' + fn() + '</b>'
    return wrapped

# 定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return '<i>' + fn() + '</i>'
    return wrapped

@makeBold
def test1():
    return 'hello-1'

@makeItalic
def test2():
    return 'hello-2'

@makeItalic
@makeBold
def test3():
    return 'hello-3'


print(test1())
print(test2())
print(test3())



'''
    装饰器
'''

# 无参的函数
def check_time(action):
    def do_action():
        action()
    return do_action

@check_time
def go_to_bed():
     print('去睡觉')

go_to_bed()



# result = check_time(go_to_bed)  # 把go_to_bed 当做参数传入给 check_time函数，再定义一个变量用来保存check_time的运行结果
# result()  # check_time 函数的返回值result是一个函数, result()再调用这个函数，让它再调用go_to_bed函数

print()

# 被装饰的函数有参数
def check_time(action):
    def do_action(a, b):
        action(a, b)
    return do_action

@check_time
def go_to_bed(a, b):
    print(f'{a}去{b}睡觉')

go_to_bed('zhangsan','chuangshang')


# 被装饰的函数有不定长参数
def test1(cal):
    def do_cal(*args, **kwargs):
        cal(*args, **kwargs)
    return do_cal

@test1
def demo(*args):
    sum = 0
    for x in args:
        sum += x
    print(sum)

demo(1,2,3,4)



