H, N = map(int, input().split())
'''
    map() 会根据提供的函数对指定序列做映射
    map(function, iterable, ...)  
    function -- 函数
    iterable -- 一个或多个序列
    第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
    迭代器：一个对象要想使用 for 的方式迭代出容器内的所有数据，这就需要这个类实现「迭代器协议」，即迭代器
'''
heights = list(map(int, input().split()))

def solution():
    heights.sort(key=lambda a: (abs(a-H), a))
    return " ".join(map(str, heights))

print(solution())

    # key参数用于指定在进行比较之前 对每个列表元素调用的函数

    '''
        匿名函数 https://www.bilibili.com/video/BV1UN4y1u7nH/?spm_id_from=333.337.search-card.all.click&vd_source=f0f606a8cf11af341bd6b055e5e180c6
        lambda x, y: x*y			# 函数输入是x和y，输出是它们的积x*y
        lambda:None					# 函数没有输入参数，输出是None
        lambda *args: sum(args)		# 输入是任意个数参数，输出是它们的和(隐性要求输入参数必须能进行算术运算)
        lambda **kwargs: 1			# 输入是任意键值对参数，输出是1
    '''
