minAverageLost = int(input())
array = list(map(int, input().split()))
'''
split() 方法会将字符串以空格分隔成一个列表，但是如果你输入 01234，则会被视为一个整体，而不是五个数字。
因此，split() 会将它作为一个字符串放在列表中的第一个元素，然后转换成整数列表时就会丢失第一个数字。
'''
result = []

# def is_append(is_add, num):
#     if not is_add:
#         index.append(num)
#     return index

index = []
summary_parts = 0
number = 1
for i in range(len(array)):
    summary_parts += array[i]
    average = summary_parts / number
    # print(f"average: {average}")
    if array[i] > minAverageLost:  # 单个数字太大
        summary_parts = 0
        number = 1
        if len(index) > 1:  # index不能只有一个数字
            index.append(i)
            result.append(f"{index[0]}-{index[-1]}")
        index.clear()
    else:
        # print(average > minAverageLost)
        # print(f"average: {average}")
        # print(f"minAverageLost: {minAverageLost}")

        if average > minAverageLost:
            summary_parts = array[i]  # 重置 summary_parts
            if len(index) > 1:
                result.append(f"{index[0]}-{index[-1]}")
            index.clear()

        elif i == len(array)-1:
            index.append(i)
            result.append(f"{index[0]}-{index[-1]}")
            # print("执行")
        else:
            index.append(i)
            # print(f"index: {index}")

        number += 1
print(*result)
'''
a = [1, 2, 3, 4, 5]
# 默认用空格分隔
print(*a)
# 用逗号分隔
print(*a, sep = ", ")
'''
