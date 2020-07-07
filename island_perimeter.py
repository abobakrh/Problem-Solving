class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        per = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    per += 4
                    if i > 0:
                        per -= grid[i-1][j]
                    if i < row - 1:
                        per -= grid[i+1][j]
                    if j > 0:
                        per -= grid[i][j-1]
                    if j < col - 1:
                        per -= grid[i][j+1]
        return per