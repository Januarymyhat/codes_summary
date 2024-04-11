num = int(input())

succeed_numbers_current = []  # 存储当前连续数的列表
succeed_numbers = []  # 存储所有满足条件的连续数列表的列表

summary = 0  # 存储当前连续数的和
i = 1
# for i in range(1, num):
while i <= num + 1:

    if summary < num:
        summary += i
        succeed_numbers_current.append(i)
        # print(succeed_numbers_current)
        i += 1

    else:

        if summary == num:
            # succeed_numbers列表中的元素不受succeed_numbers_current列表修改的影响，使用copy()副本
            succeed_numbers.append(succeed_numbers_current.copy())

            summary -= succeed_numbers_current.pop(0)
            # i += 1
            # print(succeed_numbers)

        while summary > num:
            summary -= succeed_numbers_current.pop(0)

if succeed_numbers:
    succeed_numbers.sort(key=len)
    for succeed_number in succeed_numbers:
        print(f"{num} = {'+'.join(map(str, succeed_number))}")
    print(f"Result: {len(succeed_numbers)}")

'''
def find_continuous_sum(number):
    count = 0
    expressions = []

    for i in range(1, num // 2 + 2):
        for j in range(i, num // 2 + 2):

            在循环中，我们需要考虑连续自然数之和的最小长度至少为2。
            因此，我们从1开始遍历时，需要至少有两个连续的自然数，即从1开始，考虑到2。
            因此，当我们计算到目标整数的一半时，我们需要加1以确保考虑到这个最小长度的情况，再加1是为了保证能够覆盖到目标整数本身，所以需要加2。
            
            summation = sum(range(i, j + 1))
            if summation == num:
                expression = '+'.join(str(x) for x in range(i, j + 1))
                
                range(6)输出0-5
                str(x) for x in range(i, j+1) 使用列表推导式将这个连续自然数序列中的每个数转换为字符串形式
                .join() 是字符串对象的方法，而 append() 是列表对象的方法。
                 使用 '=' 作为分隔符，将这些字符串连接起来，形成一个以 '+' 分隔的字符串，表示连续自然数序列
                 最终，expressions 变量将包含形如 "1+2+3+4" 的字符串，表示找到的连续自然数序列。
                
                expressions.append(f"{num}={expression}")
                count += 1
                break
            elif summation > num:
                break
        return expressions, count


exper, cou = find_continuous_sum(num)

for e in exper:
    print(e)
print(f"Result:{cou}")
'''

