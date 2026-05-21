class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row +dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 2147483647:
                    grid[new_row][new_col] = grid[row][col] + 1
                    queue.append((new_row, new_col))
