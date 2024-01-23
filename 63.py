from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    # TC: O(m*n)
    # SC: O(m*n)

    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]

    # paths for column 1
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            break  # you cannot go to the subsequent cells
        dp[i][0] = 1

    # paths for row 1
    for j in range(n):
        if obstacleGrid[0][j] == 1:
            break  # you cannot go to the subsequent cells
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            # curr cell is an obstacle, we cannot reach that cell
            if obstacleGrid[i][j] == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]
