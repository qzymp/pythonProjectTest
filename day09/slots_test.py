"""
slots:限定类对象只能绑定指定的属性
"""

class Person(object):

    # 限定Person对象只能绑定_name, _age, _gender 属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'{self._name}正在玩飞行棋')
        else:
            print(f'{self._name}正在玩斗地主')

def main():
    person = Person('张三', 13)
    person.play()
    person._gender = '男'
    # person._is_gay = True


if __name__ == '__main__':
    main()
