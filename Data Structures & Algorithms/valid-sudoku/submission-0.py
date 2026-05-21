class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hashset = [set() for _ in range(9)]
        col_hashset = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_hashset[r] or board[r][c] in col_hashset[c] or board[r][c] in boxes[(r // 3) * 3 + (c // 3)]:
                    return False
                row_hashset[r].add(board[r][c])
                col_hashset[c].add(board[r][c])
                boxes[(r // 3) * 3 + (c // 3)].add(board[r][c])
        return True
                
                