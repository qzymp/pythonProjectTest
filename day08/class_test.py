class Student:

    # init 用于在创建对象时，初始化的方法
    # 通过这个方法绑定名字，年龄2个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')

    def watch_tv(self):
        if self.age >= 18:
            print(f'可以看电影')
        else:
            print('看喜洋洋')

def main():
    stu1 = Student('zhangsan', 18)
    stu2 = Student('lisi', 6)

    stu1.watch_tv()
    stu2.watch_tv()

    stu1.study('python编程')
    stu2.study('数学')

if __name__ == '__main__':
    main()
