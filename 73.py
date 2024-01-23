from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # TC: O(m*n)
    # Sc: O(1)

    rows = []
    cols = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for row in rows:
        for col in range(len(matrix[0])):
            matrix[row][col] = 0

    for col in cols:
        for row in range(len(matrix)):
            matrix[row][col] = 0
