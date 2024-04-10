n_student, m_course = map(int, input().split())
courses = input().split()

students = []
for _ in range(n_student):
    students.append(list(input().split()))
rank_course = input()

if rank_course in courses:
    position = courses.index(rank_course) + 1
    sorted_students = sorted(students, key=lambda x: x[position], reverse=True)  # 需要赋值，否则白整

    # print(lambda name: students[name][0])
    # lambda 函数需要一个参数来调用。另外，你应该将 lambda 表达式传递给 print() 函数，而不是直接打印它。

    print(" ".join(map(lambda x: x[0], sorted_students)))
    # lambda x: x[0]: lambda 它可以接受任意数量的参数，但只能有一个表达式.x[0]返回参数 x 的第一个元素
    # map(lambda x: x[0], students): 这一部分的作用是将Lambda函数应用到students中的每个元素上

else:
    # 计算每个子列表的第二个元素到最后一个元素的和
    sums = [sum(map(int, student[1:])) for student in students]

    # 将新的子列表添加到原始的学生列表中
    for i in range(n_student):
        students[i].append(str(sums[i]))
    sorted_students = sorted(students, key=lambda x: x[-1], reverse=True)

    print(" ".join(map(lambda x: x[0], sorted_students)))

    '''
    错误：students.append(sum(map(lambda x: x[1:], students)))
    map() 函数返回的是一个迭代器，它不会修改原始列表。
    此外，你使用的 lambda 函数 lambda x: x[1:] 是用来取每个子列表中除了第一个元素以外的所有元素。
    如果你想要将结果添加到原始列表中，你需要使用 map() 函数生成的迭代器的值来构建一个新的子列表，然后将其添加到 students 列表中。
    但是，这样做并不简洁，也不推荐。更好的方法是使用列表推导式来完成这个任务。
    '''
