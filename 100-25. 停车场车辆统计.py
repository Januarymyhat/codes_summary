import re

'''
re.sub(pattern, repl, string)
pattern 是要匹配的正则表达式模式；
repl 是用来替换匹配项的字符串；
string 是要进行替换操作的原始字符串
'''

car_positions = input().replace(',', '')
car_positions = re.sub(r"111", "x", car_positions)
car_positions = re.sub(r"11", "x", car_positions)
car_positions = re.sub(r"1", "x", car_positions)

ans = str.count('x')
print(ans)
