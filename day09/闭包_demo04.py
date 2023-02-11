#
# def outer(n):
#     num = n
#     def inner():
#         return num+1
#     return inner
#
# print(outer(3)())  # 4
# print(outer(5)())  # 4

def outer(n):
    num = n
    def inner():
        return num+1
    return inner

print(outer(3)())  # 4
print(outer(5)())  # 5

print()

def outer(n):
    num = n
    def inner ():
        nonlocal num
        num = num + 1
        return num
    return inner

print(outer(2)())
print(outer(5)())


print('--------------------------')


def func(*args):
    # print(**kwargs)
    print(*args)

# arg_dict = {'args_1':'a', 'arg_2':'b'}
func(*[1,2])



