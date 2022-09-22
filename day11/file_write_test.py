from math import sqrt

"""
将1-9999之间的素数分别写入三个文件中（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）
"""

def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    files = ('a.txt', 'b.txt', 'c.txt')
    file_list = []
    try:
        for file in files:
            file_list.append(open(file, 'w', encoding='utf-8'))
        for num in range(1,10000):
            if is_prime(num):
                if num < 100:
                    file_list[0].write(str(num) + '\n')
                elif num < 1000:
                    file_list[1].write(str(num) + '\n')
                else:
                    file_list[2].write(str(num) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误')
    finally:
        for fs in file_list:
            fs.close()

    print('操作完成')

if __name__ == '__main__':
    main()


