string = input()
# 判断大小写string.islower()，大写string.isupper()

count = string.count('o')
if count % 2 == 0:
    print(len(string))
else:
    print(len(string) - 1)


'''
倒叙的方法：
range(len(string)-1, -1, -1)
reversed(string)
string[::-1]
'''
