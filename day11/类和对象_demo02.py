class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __del__(self):
        print('__del__方法被调用')


s = Student('zhangsan', 98)
# del s
input('请输入内容')