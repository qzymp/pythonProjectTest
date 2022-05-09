a = 34
b = 12

print((a > b) and (b > 10) and (a > 30) and (a > 50))
print((a > b) and (b > 10) and (a > 30) and (a < 50))
print(a and b and 'hello' and 0 and 123)
print(a and b and 'hello' and 123 and 'hi')

print()

print((a > 50) or (b < 10) or a > b or (a == b))
print((a > 50) or (b < 10) or a < b or (a == b))
print(0 or None or a or '')
print(0 or '' or "" or  None)

print()

a > 10 and print('hello world')
a < 10 and print('hello world')

a > 10 or print('你好世杰')
a < 10 or print('你好世杰')
