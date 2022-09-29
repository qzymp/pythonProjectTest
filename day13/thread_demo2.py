from threading import Thread, Lock
from time import sleep


class Account:
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁，才能执行后面的代码
        self._lock.acquire()
        try:
            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟存款时间
            sleep(0.01)
            # 修改账户余额
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作
            self._lock.release()
        # print(self._balance)

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []

    # 创建100个线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    # 等所有的线程都执行完毕
    for t in threads:
        t.join()

    print(f'账户余额为{account.balance}元')

if __name__ == '__main__':
    main()


