class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        // Iterate through the grid.
        // If a cell is a '1', start DFS from that cell.
        // In DFS, explore adjacent land cells and mark them as visited.
        // Keep track of the area of the current island.
        // Update the max area found so far.

        if (!grid || grid.length === 0) {
            return 0;
        }

        const ROWS = grid.length;
        const COLS = grid[0].length;
        let maxArea = 0;

        const dfs = (row, col) => {
            if (row < 0 || row >= ROWS || col < 0 || col >= COLS || grid[row][col] === 0) {
                return 0;
            }

            grid[row][col] = 0;

            let area = 1;
            area += dfs(row + 1, col);
            area += dfs(row - 1, col);
            area += dfs(row, col - 1);
            area += dfs(row, col + 1);
            return area;
        };

        for (let i = 0; i < ROWS; i++) {
            for (let j = 0; j < COLS; j++) {
                if (grid[i][j] === 1) {
                    maxArea = Math.max(maxArea, dfs(i, j));
                }
            }
        }
        return maxArea;
    }
}
