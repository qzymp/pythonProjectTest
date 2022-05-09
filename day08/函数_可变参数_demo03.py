
def test(a, b, *args, **kwargs):
    print(f'a={a}, \nb={b}, \nargs={args}, \nkwargs={kwargs}')

# test(2, 3, '你好', 'hi', 'how do you do', name="zhangsan", age=18)

a = ('hi', '大家好', '今天天气真好')
b = {'name': "zhangsan", "age": 19}

test(10, 20, a, b)



