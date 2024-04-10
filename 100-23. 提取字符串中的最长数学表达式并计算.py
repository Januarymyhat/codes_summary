import re

input_string = input()

# 使用正则表达式匹配连续的数字以及加号和减号
'''
[+-]?：匹配可选的加号或减号（+ 或 -），? 表示前面的符号出现零次或一次。
/d 表示匹配任意一个数字字符（0-9）， + 表示匹配前面的元素一次或多次
(?: ... ) 是非捕获组，它表示匹配其中的内容但不捕获为一个单独的组。
[+*/-] 表示匹配一个加号、减号、乘号或除号中的任意一个
* 表示匹配前面的元素零次或多次
'''

pattern = r'[+-]?\d+(?:[+*/-]\d+)*'
matches = re.findall(pattern, input_string)

# max_expression = max(results, key=len)
max_expression = max(matches, key=lambda x: len(str(x)))

try:
    # 使用 eval() 函数计算表达式的结果
    print(eval(max_expression))
except:
    print(0)
