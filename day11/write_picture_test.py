def main():
    try:
        o = open('图片test.png', 'rb')
        data = o.read()
        print(type(data))
        w = open('图片copy.png', 'wb')
        w.write(data)

        print('复制完成')

    except IOError as ex:
        print(ex)
        print('读取文件时出错')
    finally:
        w.close()
        o.close()

if __name__ == '__main__':
    main()



