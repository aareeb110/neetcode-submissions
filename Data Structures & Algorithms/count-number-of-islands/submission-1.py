class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islandCount = 0

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == '0':
                return
            
            grid[row][col] = '0'
            for dr, dc in directions:
                dfs(row + dr, col + dc)
            
        for i in range(ROWS):
            for j in range(COLS):
                if (grid[i][j] == '1'):
                    islandCount += 1
                    dfs(i, j)
        return islandCount