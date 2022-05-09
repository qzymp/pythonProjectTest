
sum = lambda args1, args2: args1 + args2

# 调用sum函数
# print(sum(10, 20))
# print(sum(10, 30))

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 92},
    {'name': 'lisi', 'age': 20, 'score': 90},
    {'name': 'wangwu', 'age': 19, 'score': 95},
    {'name': 'jerry', 'age': 21, 'score': 98},
    {'name': 'chris', 'age': 17, 'score': 100},
]

# 分数集合
scores = []
# 获取所有学生的分数
for student in students:
    scores.append(student.get('score'))
print(scores)
# 将分数进行排序
scores.sort(reverse=False)
print(scores)
# 分数排序后的学生集合
newStudents = []
# 将学生分数对应，装进新的列表
# 获取排序后的分数
for score in scores:
    for student in students:
        # 获取学生分数
        studentScore = student.get('score')
        # 学生分数 等于 排序后的分数
        if score == studentScore:
            newStudents.append(student)
for student in newStudents:
    print()


print()


def foo(ele):
    return ele['score']

students.sort(key=foo)


for student in students:
    print(student)

