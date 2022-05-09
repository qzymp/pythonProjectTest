class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, score):
        super(Student, self).__init__(name, age)
        self.score = score

class Dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

p = Person('zhangsan', 11)
s = Student('lisi', 22, 99)
d = Dog('wangcai', 'baise')

# isinstance    判断对象是否由某一个类（子类）实例化
print(isinstance(p, Person))
print(isinstance(s, Person))
print(isinstance(d, Person))

print()

# issubclass    判断2个类之间的继承关系
print(issubclass(Student, Person))
print(issubclass(Dog, Person))



# p1 = Person('zhangsan', 18)
# p2 = Person('zhangsan', 18)
#
# print(p1 == p2)
#
# print(p1 is p2)
#
# print(isinstance(p1, Person))
