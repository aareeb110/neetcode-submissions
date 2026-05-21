class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    orangesRotting(grid) {
        if (grid.length === 0) {
            return 0;
        }

        const rows = grid.length;
        const cols = grid[0].length;
        const queue = [];
        let freshOranges = 0;
        let minutes = 0;

        // Init queue with rotten oranges and count fresh oranges
        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                if (grid[i][j] === 2) {
                    queue.push([i, j]);
                } else if (grid[i][j] === 1) {
                    freshOranges++;
                }
            }
        }

        if (freshOranges === 0) {
            return 0;
        }

        const directions = [
            [0, 1], [0, -1], [1, 0], [-1, 0]
        ];

        while (queue.length > 0) {
            let size = queue.length;

            for (let i = 0; i < size; i++) {
                const [row, col] = queue.shift();

                // Check adjacent cells
                for (const [dr, dc] of directions) {
                    const newRow = row + dr;
                    const newCol = col + dc;

                    if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && grid[newRow][newCol] === 1) {
                        grid[newRow][newCol] = 2; // rot the orange
                        freshOranges--;
                        queue.push([newRow, newCol]); // add rotten orange to the shit
                    }
                }
            }
            if (queue.length > 0) {
                minutes++;
            }
        }
        if (freshOranges > 0) {
            return -1;
        }
        return minutes;
    }
}
