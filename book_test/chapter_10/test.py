

while True:
    num_first = input("输入第一个数字：")
    num_second = input("输入第二个数字：")
    try:
        sum = int(num_first) + int(num_second)
        print(sum)
    except ValueError:
        print("请输入数字")

