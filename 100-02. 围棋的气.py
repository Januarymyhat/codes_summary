black = list(map(int, input().split()))
white = list(map(int, input().split()))


def convert_to_coords(coords):
    return [(coords[i], coords[i + 1]) for i in range(0, len(coords), 2)]  # 开始 结束 步伐


# 转换为坐标
black_situation = convert_to_coords(black)
white_situation = convert_to_coords(white)

# 布置棋子的位置
board = [[0] * 19 for _ in range(19)]  # [[0 for _ in range(19)] for _ in range(19)]
for chess in black_situation:
    board[chess[0]][chess[1]] = 1
    # 将 black_situation 中的棋子位置在 plate 中标记为1
for chess in white_situation:
    board[chess[0]][chess[1]] = 2


def calculate_lib(n: int, board):  # 计算有多少个气
    liberty = 0

    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:  # 找到的没落棋子的位置
                # 看周围有没有棋子
                if i + 1 < 19 and board[i + 1][j] == n:
                    liberty += 1
                elif i - 1 >= 0 and board[i - 1][j] == n:
                    liberty += 1
                elif j + 1 < 19 and board[i][j + 1] == n:
                    liberty += 1
                elif j - 1 >= 0 and board[i][j - 1] == n:
                    liberty += 1
                '''
                    and: 是Python中的逻辑运算符，用于对布尔值进行逻辑与操作。只有当所有条件都为真时，整个条件表达式才为真。
                    &: 是位运算符，用于对整数进行按位与操作
                        result = a & b  # 对整数 a 和 b 进行按位与操作
                        在布尔运算中，& 也可以用于对布尔值进行逻辑与操作，但通常情况下更推荐使用 and
                '''
            else:
                continue
    return liberty


print(calculate_lib(1, board))
print(calculate_lib(2, board))
