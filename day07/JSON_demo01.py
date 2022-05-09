import json

person = {'name': 'zhangsan', 'age': 18}
x = json.dumps(person)
print(x)
print(type(x))

nums = [1, 2, 3, 34, 5, 675, 6]
y = json.dumps(nums)
print(y)
print(type(y))

words = ('hello', 'good')
z = json.dumps(words)
print(z)
print(type(z))

print()

p = '{"name": "zhangsan", "age": 18}'
person = json.loads(p)
print(person)
print(type(person))

n = '[1, 2, 3, 34, 5, 675, 6]'
nums = json.loads(n)
print(nums)
print(type(nums))