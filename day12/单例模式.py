class A(object):
    def __init__(self):
        print('init 方法')

    def __new__(cls, *args, **kwargs):
        print('new 方法')
        return object.__new__(cls)

A()

print()

# 单例模式
class Singleton(object):
    __instance = None
    __is_first = True

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance =  object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if self.__is_first:
            # 是第一个
            self.name = name
            self.age = age
            Singleton.__is_first = False

a = Singleton(19, 'zhangsan')
b = Singleton(22, 'lisi')
print(id(a))
print(id(b))

print(a.age)
print(b.age)

a.age = 99
print(b.age)
