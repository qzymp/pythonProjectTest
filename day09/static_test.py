from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 判断是否为三角形
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    # 计算周长
    def perimeter(self):
        return self._a + self._b + self._c

    # 计算面积
    def area(self):
        # 一半周长
        half = self.perimeter() / 2
        # 计算面积
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    # 判断是否是三角形
    if Triangle.is_valid(a, b, c):
        # 是三角形
        t = Triangle(a, b, c)
        # 计算周长
        print(t.perimeter())
        # 计算面积
        print(t.area())

if __name__ == '__main__':
    main()

