def uniquePaths(m: int, n: int) -> int:
    # TC: O(m*n)
    # SC: O(m*n)

    dp = [[0 for j in range(n)] for i in range(m)]

    # paths for column 1
    for i in range(m):
        dp[i][0] = 1

    # paths for row 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]
