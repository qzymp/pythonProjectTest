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


