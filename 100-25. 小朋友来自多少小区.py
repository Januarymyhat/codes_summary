# 可以使用集合（Set）来筛选出输入中的不同数字。
garden = set(input().split())

'''
错误print(sum(garden) + len(garden))
garden 是一个集合（set），而集合并不支持像列表那样的迭代器，因此你不能直接对集合使用 sum() 函数
'''

print(sum(map(int, garden)) + len(garden))
