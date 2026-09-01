class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])
        for j in range(9):
            column = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in column:
                    return False
                column.add(board[i][j])
        for i in range(9):
            square = set()
            for j in range(3):
                for k in range(3):
                    r = (i // 3) * 3 + j
                    c = (i % 3) * 3 + k
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in square:
                        return False
                    square.add(board[r][c])
        return True
