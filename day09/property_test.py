"""
@property   装饰器
"""

class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name


    def play(self):
        if self._age <= 16:
            print(f'{self._name}正在玩飞行棋')
        else:
            print(f'{self._name}正在斗地主')

def main():
    person = Person('张三',12)
    person.name = '李四'
    person.play()
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()

