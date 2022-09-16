from time import sleep


class Clock:

    # 初始化
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # 显示时间
    def show(self):
        return f'{self.hour}:{self.minute}:{self.second}'

    # 走字
    def run(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    self.hour = 0


def main():
    clock = Clock(23,59,11)
    while True:
        print(clock.show())
        clock.run()
        sleep(1)


if __name__ == '__main__':
    main()



