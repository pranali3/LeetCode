class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # TC: O(m*n)
        # SC: O(m*n)

        m = len(grid)
        n = len(grid[0])

        totalCost = [[0 for j in range(n)] for i in range(m)]
        totalCost[0][0] = grid[0][0]

        # Initialize first column of total cost(TC) array
        for i in range(1, m):
            totalCost[i][0] = totalCost[i - 1][0] + grid[i][0]

        # Initialize first row of tc array
        for j in range(1, n):
            totalCost[0][j] = totalCost[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                totalCost[i][j] = min(totalCost[i - 1][j], totalCost[i][j - 1]) + grid[i][j]
        return totalCost[m - 1][n - 1]
