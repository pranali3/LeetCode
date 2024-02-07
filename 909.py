def snakesAndLadders(board: List[List[int]]) -> int:
    # TC: O(n*n*(V+E))

    length = len(board)
    board.reverse()

    def intToPos(square):
        r = (square - 1) // length
        c = (square - 1) % length
        if r % 2:
            c = length - 1 - c
        return [r, c]

    q = deque()
    q.append([1, 0])  # [square, moves]
    visit = set()
    visit.add(1)

    while q:
        square, moves = q.popleft()
        for i in range(1, 7):
            nextSquare = square + i
            r, c = intToPos(nextSquare)
            if board[r][c] != -1:
                nextSquare = board[r][c]
            if nextSquare == length * length:
                return moves + 1
            if nextSquare not in visit:
                visit.add(nextSquare)
                q.append([nextSquare, moves + 1])
    return -1
