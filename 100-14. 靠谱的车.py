import sys
# python3中使用sys.stdin.readline()可以实现标准输入，其中默认输入的格式是字符串，如果是int，float类型则需要强制转换。
N = sys.stdin.readline().strip()
index = 0
offset = 0  # 一个偏移量
before_offset = 0

while index < len(N):
    n = N[len(N) - 1 - index]  # 获取从右向左数第index位的数字
    if n != "0":
        # 如果当前数字不为0，则将该数字乘以before_offset，并加到偏移量offset上
        offset += int(n) * before_offset
        if n > "4":
            # 当前处理的数字之后的所有位数组成的数字（全部置为9），再加上一个额外的1,以弥补当前位数之后的所有位数都设置为9所带来的损失
            offset += 10 ** index - before_offset
    before_offset = before_offset * 9 + 10 ** index
    index += 1


"""
for i in range(1, in_output + 1):
    temp = i
    fake_output = ""  # 清空 fake_output

    if i + difference == in_output:
        print(i)
        break

    while temp > 0:
        digit = temp % 10
        if digit == 4:
            # real_number = i
            fake_output = "5" + fake_output
            difference += 10 ** (len(fake_output) - 1)
            # print("执行")
            print(f"difference: {difference}")
            print(f"fake_output: {fake_output}")
        else:
            fake_output = str(digit) + fake_output
        temp //= 10

    
    如果下一个真正的数字是15，那么输出依然是15。
    因为每个数字都是独立计费的，无论前面的数字是什么，只要当前数字是15，实际产生的费用就是15。
    所以不需要更新i：
    if i != int(fake_output):

        i = int(fake_output)  # 重新计算 i 的值
        # print(fake_output) checked
        continue
    # print(i) checked
"""
