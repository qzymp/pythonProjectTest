class Person:

    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __str__(self):
        return f'姓名：{self.name},年龄：{self.age}'


p1 = Person('zhangsan', 18)
p1.name = 'lisi'
# p2 = Person('zhangsan', 18)
# p3 = Person('lisi', 22)

print(p1)
