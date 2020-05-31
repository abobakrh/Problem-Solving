class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        total = 0
        row_len = len(matrix)
        col_len = len(matrix[0])
        ans_mat = [ [0]*(col_len + 1) for _ in range(row_len + 1) ]
        print(ans_mat)
        for i in range(1,row_len + 1):
            for j in range(1,col_len + 1):
                if matrix[i - 1][j - 1] == 1:
                    ans_mat[i][j] = 1 + min(ans_mat[i - 1][j] , ans_mat[i][j - 1] , ans_mat[i - 1][j - 1])
                    total += ans_mat[i][j]
        print(ans_mat)
        return total
        