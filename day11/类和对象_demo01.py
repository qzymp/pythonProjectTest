class Cat:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name}爱吃鱼')

    def drink(self):
        print(f'{self.name}猫喝水')

tom = Cat('Tom')
tom.eat()
tom.drink()

