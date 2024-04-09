planes = input().split(',')

'''
错误output = planes.sort(key = plane[0:1])  # sort() 方法中的key参数应该接受一个函数，而不是直接的切片

lambda arguments参数: expression返回值

planes.sort(key=lambda plane: plane[:2])  # 这里的 [:2] 表示从索引0开始，一直取到索引1的字符，但不包括索引2的字符
错误
planes.sort(key=lambda plane: plane[2:])
'''
# 这样，列表会首先按照飞机字符串的前两个字符进行排序，然后再按照第三个字符到最后的字符进行排序
planes.sort(key=lambda plane: (plane[:2], plane[2:]))

print(','.join(planes))
