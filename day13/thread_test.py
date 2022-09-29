import random
from threading import Thread
from time import sleep, time


def download(filename):
    print(f'开始下载{filename}')
    time_to_download = random.randint(5, 10)
    sleep(time_to_download)
    print(f'下载完成，耗费了{time_to_download}秒')

def main():
    start = time()

    t1 = Thread(target=download, args=('python从入门到入土.pdf',))
    t1.start()

    t2 = Thread(target=download, args=('Java从入门到住院.pdf',))
    t2.start()

    t1.join()
    t2.join()

    end = time()

    print(f'总共花费了{end - start}秒')

if __name__ == '__main__':
    main()



