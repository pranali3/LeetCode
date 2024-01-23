def wallsAndGates(self, rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    if not rooms:
        return

    rows, cols = len(rooms), len(rooms[0])
    visit = set()

    def get_nbr(row, col):
        result = []

        if row - 1 >= 0:
            result.append((row - 1, col))
        if col - 1 >= 0:
            result.append((row, col - 1))
        if row + 1 < rows:
            result.append((row + 1, col))
        if col + 1 < cols:
            result.append((row, col + 1))

        return result

    def dfs(r, c, count):
        visit.add((r, c))
        rooms[r][c] = min(rooms[r][c], count)

        # directions = [[0,-1], [0,1], [-1,0], [1,0]]
        # print(r,c)
        for row, col in get_nbr(r, c):
            if ((row, col) not in visit):
                if rooms[row][col] > 0:
                    dfs(row, col, count + 1)

        visit.remove((r, c))

    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:  # 0: gate
                dfs(r, c, 0)
