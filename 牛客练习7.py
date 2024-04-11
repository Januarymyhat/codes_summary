'''
输入描述：
输入数据有多组, 每行表示一组输入数据。

每行不定有n个整数，空格隔开。(1 <= n <= 100)。
输出描述：
每组数据输出求和的结果
示例1
输入例子：
1 2 3
4 5
0 0 0 0 0
输出例子：
6
9
0
'''

while True:
    try:
        # 读取一行输入并将其转换为整数列表
        numbers = list(map(int, input().split()))
        # 计算整数列表的和并输出结果
        print(sum(numbers))
    except EOFError:
        # 如果没有更多的输入，则结束循环
        break

'''
EOFError 是 Python 中的一种异常类型，它代表着 "End of File Error"，即文件结束错误。
在 Python 中，当使用一些输入函数（如 input() 或者 file.readline()）从标准输入或文件中读取数据时，
如果已经读取到文件末尾，再次尝试读取数据就会引发 EOFError 异常。
