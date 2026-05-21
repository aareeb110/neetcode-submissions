class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const m = matrix.length;
        const n = matrix[0].length;

        let L = 0;
        let R = m * n - 1;
        while (L <= R) {
            const mid = L + Math.floor((R - L) / 2);
            const row = Math.floor(mid / n);
            const col = mid % n;

            if (matrix[row][col] < target) {
                L = mid + 1;
            } else if (matrix[row][col] > target) {
                R = mid - 1;
            } else {
                return true;
            }
        }
        return false;

    }
}
