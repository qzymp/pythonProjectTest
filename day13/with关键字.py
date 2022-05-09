def m1():
    file = open('output.txt', 'w')

    try:
        file.write('python入土')
    except IOError:
        print('oops error')
    finally:
        file.close()

# m1()


def m2():
    with open('output.txt', 'w') as file:
        file.write('py')

# m2()




