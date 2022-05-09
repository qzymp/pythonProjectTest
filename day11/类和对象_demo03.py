class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self) -> str:
        return 'haha'


tom = Cat('tom', 'white')
print(tom)
