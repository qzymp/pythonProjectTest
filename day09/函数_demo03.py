def test():
    return 'hello world'

print(type(test))   # <class 'function'>

print()

fun = test
print(fun())

print(id(fun))
print(id(test))

print()

def smoke():
    print('18岁，可以抽烟')

my_action = smoke

def test1(age, action):
    if age > 18:
        action()
    else:
        print('不满18岁，不能抽烟')

test1(110, smoke)
