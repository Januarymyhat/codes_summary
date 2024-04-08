N = int(input())
words = []
for _ in range(N):
    words.append(input())
chars = input()
# 无论用户输入的是数字、字母还是其他字符，input() 函数都会将其作为字符串处理
output = 0

for word in words:
    length = len(word)
    temp = chars
    c = 0

    for i in range(length):
        if word[i] in temp:
            # 在 temp 列表中查找 word[i] 所代表的元素的索引位置
            index = temp.index(word[i])
            # 移除了列表 temp 中索引位置为 index 的元素，相当于从列表中删除了这个元素
            temp = temp[:index] + temp[index + 1:]
            c += 1

    if '?' in chars:
        # chars.count('?')统计字符串chars中字符'?'出现的次数
        if length - c <= chars.count('?') or length == c:
            output += 1
    else:
        if length == c:
            output += 1

print(output)
