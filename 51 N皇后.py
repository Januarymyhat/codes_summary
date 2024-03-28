class Solution(object):
    def solveNQueens(self, n:int) -> List[List[str]]:
      #self指向创建的实例本身 https://blog.csdn.net/CLHugh/article/details/75000104
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = [] # 存储最终结果的二维字符串数组
      
        board = ['.' * n for _ in range(n)] # 初始化棋盘
        '''
        在Python中，通常使用 _ 作为一个临时变量名或占位符。
        它的含义是告诉读者，该变量的值在当前上下文中不会被使用，或者该变量的值不重要。
        在你提供的代码中，_ 被用作列表推导式中的循环变量，表示在循环中不需要使用该变量的值。
        '''
        self.backtrack(n,0,board,result)
        return [[''.join(row) for row in solution] for solution in result]

    def backtrack(self, n, row, board, result:List[List[str]]) -> None:
        if row == n:
            result.append(board[:]) # 棋盘填满，将当前解加入结果集
            return
        
        for col in range(n):
            if self.isValid(row, col, board):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]  # 放置皇后
                self.backtracking(n, row + 1, chessboard, result)  # 递归到下一行
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]  # 回溯，撤销当前位置的皇后


    def isValid(self, row:int, col:int, board:List[str]) -> bool:
         # 检查列
        for i in range(row):
            if board[i][col] == 'Q':
                return False # 当前列已经存在皇后，不合法

        # 检查 45 度角是否有皇后
        i,j = row-1, col-1
        while i >= 0 and j >=0:
            if board[i][j] == 'Q':
                return False # 左上方向已经存在皇后，不合法
            i -=1
            j -=1

         # 检查 135 度角是否有皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < len(board):
            if chessboard[i][j] == 'Q':
                return False  # 右上方向已经存在皇后，不合法
            i -= 1
            j += 1
        
        return True # 当前位置合法
