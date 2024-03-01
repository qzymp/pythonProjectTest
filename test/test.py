from random import randrange, randint
from collections import Counter

# print(randrange(4))


# items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
# print(items1)sada


# LOGID_BATTLE_CHAT_FLOW|1.1.14.1|2022-10-19 19:45:58|GU_1131|1|1001|67601510198587|0|30|eb3b351dbd238bd2e939cddd672e6bf3|3146137716661796911|25|\
#                                                  114+1,112+1,111+1,113+1,115+1,104+1,102+1,101+1,103+1,105+1,10+2,109+1,7+3,107+1,6+2,106+1,9+3,108+1,11+2,110+1,120+1,118+1,116+1,119+2,117+1


# LOGID_BATTLE_CHAT_FLOW|1.1.14.1|2022-10-19 19:45:58|GU_1131|1|1001|67627682655547|0|30|47231eaa62abe939b3c06a085bbf0183|3146137716661796911|25|\
#                                                 114+1,112+1,111+1,113+1,115+1,104+1,102+1,101+1,103+1,105+1,10+2,109+1,7+3,107+1,6+2,106+1,9+3,108+1,11+2,110+1,120+1,118+1,116+1,119+2,117+1


prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        # scores[row][col] = float(input(f'请输入{name}的{course}成绩：'))
        print(scores)

# 找出序列中出现次数最多的元素
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(1))


def select_sort(items):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] > items[min_index]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]

    print(items)


def bubble_sort(items, comp=lambda x,y: x > y):
    """冒泡排序"""




if __name__ == '__main__':
    list = [1, 4, 2, 5, 6, 0, 0]
    select_sort(list)
