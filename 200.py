import collections
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    # O(m*n*(V+E))
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def bfs(r, c):  # O(V+E)
        visit.add((r, c))
        q = collections.deque()
        q.append((r, c))

        while q:
            r, c = q.popleft()

            directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(rows) and col in range(cols) and
                        grid[row][col] == "1" and (row, col) not in visit):
                    q.append((row, col))
                    visit.add((row, col))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1
    return islands
