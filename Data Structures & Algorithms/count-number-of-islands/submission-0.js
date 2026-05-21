class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        // Iterate through each cell of the grid
        // If a cell is '1' then it is land, and we can increment an island count.
        // We can use DFS to traverse this grid, marking all connected land cells as visited.

        let ROWS = grid.length;
        let COLS = grid[0].length;
        const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

        let islandCount = 0;

        const dfs = (row, col) => {
            if (row < 0 || row >= ROWS || col < 0 || col >= COLS || grid[row][col] === '0') {
                return;
            }

            grid[row][col] = '0';
            for (const [dr, dc] of directions) {
                dfs(row + dr, col + dc);
            }
        };
        
        for (let i = 0; i < ROWS; i++) {
            for (let j = 0; j < COLS; j++) {
                if (grid[i][j] === '1') {
                    islandCount++;
                    dfs(i, j);
                }
            }
        }
        return islandCount;
    }
}
