class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        cols = len(grid[0])

        for i in range(row):
            for j in range(cols):
                if i == 0 and j == 0:
                    grid[i][j] = grid[i][j]
                elif i != 0 and j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                elif i == 0 and j != 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
        return grid[row-1][cols-1]