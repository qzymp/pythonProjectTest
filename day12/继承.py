class Animal:
    def __init__(self):
        pass

    '''动物类'''
    def sleep(self):
        print('睡觉')

class Dog(Animal):
    '''Dog类继承Animal类'''
    def __init__(self):
        pass

    def sleep(self):
        print('狗睡觉')

class Cat(Animal):
    '''Cat类继承Animal类'''
    def __init__(self):
        pass

dog = Dog()
dog.sleep()

cat = Cat()
cat.sleep()