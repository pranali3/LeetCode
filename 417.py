def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    # TC: O(n*m)

    rows, cols = len(heights), len(heights[0])
    pacVisit, atlVisit = set(), set()
    res = []

    def dfs(r, c, visit, prevHeight):
        if ((r, c) in visit or r not in range(rows) or c not in range(cols) or
                heights[r][c] < prevHeight):
            return
        visit.add((r, c))
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])

    for c in range(cols):
        # top row
        dfs(0, c, pacVisit, heights[0][c])
        # bottom row
        dfs(rows - 1, c, atlVisit, heights[rows - 1][c])

    for r in range(rows):
        # left col
        dfs(r, 0, pacVisit, heights[r][0])
        # right col
        dfs(r, cols - 1, atlVisit, heights[r][cols - 1])

    for r in range(rows):
        for c in range(cols):
            if (r, c) in pacVisit and (r, c) in atlVisit:
                res.append([r, c])
    return res
