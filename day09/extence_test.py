class Person:
    """人"""
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
        print(f'{self._name}正在愉快的玩耍')

    def watch_tv(self):
        if self._age >= 18:
            print(f'{self._name}正在看电影')
        else:
            print(f'{self.name}正在看动画片')

class Student(Person):
    """学生"""
    def __init__(self, name, age, grade):
        # self.name = name
        # self.age = age
        super(Student, self).__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print(f'{self._grade}的{self._name}正在学习{course}')


class Teacher(Person):
    """老师"""
    def __init__(self, name, age, title):
        super(Teacher, self).__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print(f'{self._name}{self._title}正在讲{course}')

def main():
    stu = Student('张三', 18, '初三')
    stu.study('python')
    stu.watch_tv()

    t = Teacher('李四', 30, '砖家')
    t.teach('python程序设计')
    t.watch_tv()
    t.age = 89
    print(t.age)

if __name__ == '__main__':
    main()




