class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            if board[i][0] == 'O' :
                self.aho(board,i,0)
            if board[i][cols - 1] == 'O' :
                self.aho(board,i,cols - 1)
        for j in range(cols):
            if board[0][j] == 'O':
                self.aho(board,0,j)
            if board[rows - 1][j] == 'O':
                self.aho(board,rows - 1,j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'
    def aho(self,board,i,j):
        rows = len(board)
        cols = len(board[0])
        if board[i][j] == 'O':
            board[i][j] = '*'
        if i > rows - 1 or i < 0 or j > cols or j < 0:
            return
        if i > 0 and board[i - 1][j] == 'O' :
            self.aho(board,i - 1,j)
        if i < rows - 1 and board[i + 1][j] == 'O':
            self.aho(board,i + 1,j)
        if j > 0 and board[i][j-1] == 'O':
            self.aho(board,i,j - 1)
        if j < cols - 1 and board[i][j+1] == 'O':
            self.aho(board,i,j + 1)