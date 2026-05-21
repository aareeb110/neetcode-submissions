class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        atlantic_reachable = set()
        pacific_reachable = set()

        def dfs(row, col, reachable):
            if (row, col) in reachable:
                return
            reachable.add((row, col))

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, reachable)
        
        for col in range(cols):
            dfs(rows - 1,  col, atlantic_reachable)
        for row in range(rows):
            dfs(row, cols - 1, atlantic_reachable)
        
        for col in range(cols):
            dfs(0, col, pacific_reachable)
        for row in range(rows):
            dfs(row, 0, pacific_reachable)
        
        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific_reachable and (row, col) in atlantic_reachable:
                    result.append([row, col])
        return result