# isinstance()：判断一个对象是否是 iterable 对象
from collections.abc import Iterable

print(isinstance([], Iterable))

print(isinstance({}, Iterable))

print(isinstance('aaa', Iterable))

print(isinstance(111, Iterable))



