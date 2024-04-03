rows = int(input())
row_context = []
count = 0

for _ in range(rows):
    row_context.append(list(map(str, input().split('/'))))
    # 但是你在尝试赋值之前没有在列表中添加足够的元素，这会导致索引超出范围的错误。使用 append 方法添加元素到列表中，而不是通过索引赋值。

level, keyword = map(str, input().split())
level = int(level)
'''
你在之前的代码中并没有检查输入的 level 是否在合法的范围内，而且你使用了 int() 来将其转换为整数，这可能导致 IndexError。
你可以添加一些检查来确保 level 在合法范围内，并且可以在转换之前先检查它是否有效。
'''

for row in range(rows):
    # 检查当前行的长度是否足够
    if (1 <= level <= rows
            and len(row_context[row]) > level
            and row_context[row][level] == keyword):
        count += 1

print(count)
