def divid(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


result = divid(5, 2)
print(result)

print()

def function():
    # return [1,2,3]
    # return (1, 2, 3)
    return {'num1': 1, 'num2': 2}

# print(function())

def my_info():
    high = 180
    weight = 100
    age = 18
    return high, weight, age


print(my_info())
my_high, my_weight, my_age = my_info()
print(my_high)
print(my_weight)
print(my_age)


