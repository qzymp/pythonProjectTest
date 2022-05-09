
try:
    file = open('a.txt', 'r')

    print(file.read())
except FileNotFoundError:
    print('文件没有找到')



try:
    file = open('a.txt')
    try:
        while True:
            row = file.readline()
            if len(row) == 0:
                break
            print(row)
    except:
        # 如果在读取文件中，出现了异常，会捕获到
        pass
    finally:
        file.close()
        print('关闭文件')
except:
    print('没有这个文件')

