# isinstance()：判断一个对象是否是 iterable 对象
from collections.abc import Iterable

print(isinstance([], Iterable))

print(isinstance({}, Iterable))

print(isinstance('aaa', Iterable))

print(isinstance(111, Iterable))


print()

class Demo(object):
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

demo = Demo(10)
print(isinstance(demo, Iterable))

for d in demo:
    print(d)



