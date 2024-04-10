number = int(input())


def find_continuous_sequence(n):
    result = []
    start = 1
    end = 2
    while start < n:
        # 计算从start到end的连续正整数序列的和
        total = (start + end) * (end - start + 1) // 2
        if total == n:
            # 如果和等于n，则记录该序列
            result.append(list(range(start, end + 1)))
            start += 1
        elif total < n:
            # 如果和小于n，则增加end
            end += 1
        else:
            # 如果和大于n，则增加start
            start += 1
    return result


def min_continuous_sequence(n):
    sequences = find_continuous_sequence(n)
    if sequences:
        # 找到所有分解序列后，取长度最小的序列
        min_sequence = min(sequences, key=len)
        return f"{n}={'+'.join(map(str, min_sequence))}"
    else:
        return "N"


# 测试
print(min_continuous_sequence(number))  # 输出: 21=10+11

'''
summary = 0
summaries = []
one_summary = []   
两个循环会导致在很多情况下找到的序列不是连续的正整数序列
for i in range(number):
    for j in range(i, number):
        if summary <= number:
            summary += j
            one_summary.append(j)
            if summary == number:
                summaries.append(one_summary)
        else:
            summary = 0
            one_summary.clear()
        print(one_summary)

min_summary = min(summaries, key=len)
print(f"{number}=" + '+'.join(map(str, min_summary)))  # 方法要求列表中的元素都是字符串类型

 '''
