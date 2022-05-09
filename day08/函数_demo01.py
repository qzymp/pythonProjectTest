

def sumTest(a=1, b=2):
    sum = a + b
    return sum


def main():
    s = sumTest()
    print(s)


if __name__ == '__main__':
    main()
    help(sumTest())