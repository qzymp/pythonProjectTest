from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    # 抽象方法
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass

class Dog(Pet):
    """狗"""

    def make_voice(self):
        print(f'{self._nickname}:汪汪汪......')

class Cat(Pet):
    """猫"""

    def make_voice(self):
        print(f'{self._nickname}:喵...喵...')

def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()

