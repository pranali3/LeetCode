from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    # TC: O(n*m*4^len(word))
    # SC: O(1)
    # backtracking

    rows, cols = len(board), len(board[0])
    visited = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r, c) in visited):
            return False

        # found char word[i] at (r,c)
        visited.add((r, c))
        res = (dfs(r + 1, c, i + 1) or
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1))

        # no longer visiting (r,c)
        visited.remove((r, c))
        return res

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):  # O(m*n*dfs)
                return True
    return False
