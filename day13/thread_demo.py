import random
from threading import Thread
from time import sleep, time


class DownloadTask(Thread):
    
    def __init__(self, filename):
        super(DownloadTask, self).__init__()
        self._filename = filename

    def run(self) -> None:
        print(f'开始下载{self._filename}')
        time_to_dowmload = random.randint(5, 10)
        sleep(time_to_dowmload)
        print(f'下载完成，耗费{time_to_dowmload}秒')


def main():
    start = time()

    t1 = DownloadTask('python从入门到入土')
    t1.start()

    t2 = DownloadTask('Java从入门到住院')
    t2.start()

    t1.join()
    t2.join()

    end = time()
    print(f'总共花费了{end - start}秒')

if __name__ == '__main__':
    main()


