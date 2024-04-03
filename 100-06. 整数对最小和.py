import array

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
size1 = list1[0]
size2 = list1[0]
array1 = sorted(array.array('i', list1[1:]), reverse=False)
array2 = sorted(array.array('i', list1[1:]), reverse=False)

num = int(input())

print(sum(list(array1[:num])) + sum(list(array2[:num])))
# sum() 函数通常用于对列表等可迭代对象进行求和，而不是用于数组


'''
1.存储方式：
    list 是Python内置的数据类型，用于存储任意类型的对象，可以动态改变大小。
    array 是Python标准库中的一个模块，提供了一个类似于数组的数据类型，但要求所有元素具有相同的数据类型。
2.元素类型：
    list 中的元素可以是不同类型的对象，例如整数、字符串、列表等。
    array 中的元素必须具有相同的数据类型，例如整数数组、浮点数数组等。当创建数组时，需要指定元素的数据类型。

array 适用于需要存储大量相同类型的数据，并且对内存占用和性能有一定要求的情况。而 list 则更加灵活，适用于存储各种类型的数据，并且支持动态改变大小。
'''
