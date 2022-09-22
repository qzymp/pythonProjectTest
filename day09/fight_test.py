from abc import abstractmethod
from random import randint, randrange


class Fighter(object):
    """战斗者"""

    # 通过 slots 限定对象可以绑定的成员
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        初始化方法
        :param name:名字
        :param hp:血量
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
        攻击
        :param other: 被攻击对象
        :return:
        """
        pass

class Ultraman(Fighter):

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super(Ultraman, self).__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """
        救济必杀技，打掉对方50点或3/4血
        :param other:被攻击对象
        :return:使用成功返回True，否则False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """
        魔法攻击
        :param others:被攻击的群体
        :return:使用成功返回True，失败False
        """
        if self._mp >= 20:
            self._mp -= 20
            for other in others:
                if other.alive:
                    other.hp -= randint(15, 20)
            return True
        else:
            return False

    def resume(self):
        """
        恢复魔法值
        :return:增加的魔法值
        """
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return f'{self._name}奥特曼\n  生命值：{self._hp}\n  魔法值：{self._mp}'

class Monster(Fighter):
    """小怪兽"""

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        super(Monster, self).__init__(name, hp)

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return f'{self.name}小怪兽\n  生命值：{self.hp}\n'


def is_any_alive(monsters):
    """判断有没有小怪兽活着"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_any_alive(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('张三', 1000, 120)
    m1 = Monster('李四', 250)
    m2 = Monster('王五', 500)
    m3 = Monster('赵六', 750)
    ms = [m1, m2, m3]

    fight_round = 1
    while u.alive and is_any_alive(ms):
        print(f'======第{fight_round}回合======')
        # 选一只小怪兽
        monster = select_any_alive(ms)
        # 使用随机数选择使用哪种技能
        skill = randint(1, 10)
        if skill <= 6:
            # 60%概率使用普通攻击
            print(f'{u.name}使用普通攻击打了{monster.name}')
            u.attack(monster)
            # 恢复魔法值
            print(f'{u.name}的魔法值恢复了{u.resume()}点')
        elif skill <= 9:
            # 30%概率使用魔法攻击
            if u.magic_attack(ms):
                print(f'{u.name}使用了魔法攻击')
            else:
                print(f'{u.name}使用魔法攻击失败')
        else:
            # 10%概率使用究极必杀技
            if u.huge_attack(monster):
                print(f'{u.name}使用究极必杀技虐了{monster.name}')
            else:
                print(f'{u.name}使用普通攻击打了{monster.name}')
                print(f'{u.name}的魔法值恢复了{u.resume()}')

        if monster.alive:
            # 小怪兽还活着，攻击奥特曼
            monster.attack(u)
            print(f'{monster.name}回击了{u.name}')

        display_info(u, ms)
        fight_round += 1

    print('\n=====战斗结束=====\n')

    if u.alive:
        print(f'{u.name}奥特曼胜利')
    else:
        print('小怪兽胜利')

if __name__ == '__main__':
    main()




    





