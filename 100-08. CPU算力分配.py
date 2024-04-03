A_num, B_num = map(int, input().split())
A_calculate = list(map(int, input().split()))
B_calculate = list(map(int, input().split()))
'''
B_calculate = list(map(int, input().split())).sort()
sort() 方法在原地对列表进行排序，并返回 None，而不是返回排序后的列表。
因此，当你将其赋值给 A_calculate 后，A_calculate 实际上是 None。
'''
A_calculate.sort() # 默认升序
B_calculate.sort()
A_sum = sum(A_calculate)
B_sum = sum(B_calculate)

# 根据总算力的差值，计算出需要交换的差值的一半
average = (A_sum + B_sum) // 2
value = abs(average - A_sum)  # A差多少

if A_sum > B_sum:
    for i in A_calculate:  # i是A_calculate中的值
        if (i - value) in B_calculate:  # B_calculate存在能换的值
            print(i, i - value)
            break
else:
    for i in A_calculate:
        if (i + value) in B_calculate:  # B_calculate存在能换的值
            print(i, i + value)
            break


'''
i, j = 0, 0
while i < A_num and j < B_num:
    if A_sum - A_calculate[i] + B_calculate[j] == B_sum - B_calculate[j] + A_calculate[i]:
        print(A_calculate[i], B_calculate[j])
        
        假设从 A 组中选出一个 CPU，算力为 A_calculate[i]，从 B 组中选出一个 CPU，算力为 B_calculate[j]，然后交换它们。
        这样，A 组的总算力会减去 A_calculate[i]，然后加上 B_calculate[j]，而 B 组的总算力会减去 B_calculate[j]，然后加上 A_calculate[i]。
        但是在输入
        1 2
        2
        1 3
        得不到答案
        
        break
    elif A_sum - A_calculate[i] + B_calculate[j] < B_sum - B_calculate[j] + A_calculate[i]:
        i += 1
    else:
        j += 1
'''
