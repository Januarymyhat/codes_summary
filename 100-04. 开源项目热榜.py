how_many_people = int(input())
weights = list(map(int, input().split()))

hits = dict()


def calculate(list1, list2):
    result = 0  # 确保了 result 变量在第一次循环时已经存在，并且被初始化为0
    for i in range(len(list1)):
        result += list1[i] * list2[i]
    return result


for _ in range(how_many_people):
    name_value = list(map(str, input().split()))
    name = name_value[0]
    value = list(map(int, name_value[1:]))
    value_weight = calculate(value, weights)
    '''
    value = int(name_value[1:]) 错误 
    会导致 ValueError 错误，因为这个子字符串可能不是一个有效的整数表示
    '''
    hits.update({name: value_weight})

sorted_hits = sorted(hits.items(), key=lambda item: item[1], reverse=True)
'''
sorted() 函数用于对字典的键值对进行排序，输出的是列表，其中每个元素都是一个元组，这个元组包含了原始字典 hits 中的键值对
items() 方法用于以列表返回字典的键值对（元组形式）
在 sorted() 函数中，你可以通过 key 参数传入一个函数，该函数用于生成每个元素的排序关键字
    在上面的例子中，我们使用了一个 lambda 函数作为 key 参数，根据字典的值进行排序
item是lambda函数的参数名，它表示了字典的每个键值对。
item[1]表示对于每个键值对，取其第二个元素，也就是字典中的值。
    Python中，字典的items()方法会返回一个包含键值对的元组，元组的第一个元素是键，第二个元素是对应的值。
    因此，item[1]表示对于每个键值对，取出其值部分。
'''

for key, value in sorted_hits:
    print(key)

