# 类方法
class Dog(object):
    __type = '狗'

    # 类方法，用 classmethod 修饰
    @classmethod
    def get_type(cls):
        return cls.__type

print(Dog.get_type())

# 静态方法
class Cat(object):
    type = '猫'

    def __init__(self):
        name = None

    # 静态方法
    @staticmethod
    def introduce():
        print('猫科动物......')

cat1 = Cat()
cat1.introduce()
Cat.introduce()

