class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        grid=[[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele == ".":
                    continue
                elif ele in rows[i] or ele in cols[j] or ele in grid[i//3][j//3]:
                    return False
                else:
                    rows[i].add(ele)
                    cols[j].add(ele)
                    grid[i//3][j//3].add(ele)
        return True