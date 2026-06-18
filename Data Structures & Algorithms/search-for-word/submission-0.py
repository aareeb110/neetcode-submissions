class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[-1])
        
        def dfs(r, c, k, visited):
            # base case: if we've matched all characters of the word
            if k == len(word): return True

            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or board[r][c] != word[k]:
                return False

            visited.add((r, c))

            found = (dfs(r + 1, c, k + 1, visited) or
                    dfs(r - 1, c, k + 1, visited) or
                    dfs(r, c + 1, k + 1, visited) or
                    dfs(r, c - 1, k + 1, visited)
                    )
            visited.remove((r, c))

            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True
        
        return False
