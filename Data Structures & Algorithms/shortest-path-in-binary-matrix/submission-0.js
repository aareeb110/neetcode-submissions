class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    shortestPathBinaryMatrix(grid) {
        const n = grid.length;
        if (grid[0][0] === 1 || grid[n - 1][n - 1] === 1) {
            return -1;
        }

        const directions = [
            [0, 1], [0, -1], [1, 0], [-1, 0],
            [1, 1], [1, -1], [-1, 1], [-1, -1]
        ];

        const queue = [[0, 0, 1]];
        grid[0][0] = 1;

        while (queue.length > 0) {
            const [row, col, pathLength] = queue.shift();

            if (row === n - 1 && col === n - 1) {
                return pathLength;
            }

            for (const [dr, dc] of directions ) {
                const newRow = row + dr;
                const newCol = col + dc;

                if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < n && grid[newRow][newCol] === 0) {
                    queue.push([newRow, newCol, pathLength + 1]);
                    grid[newRow][newCol] = 1;
            }
        }
    }
    return -1;
}
}
