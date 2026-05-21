class Solution {
    /**
     * @param {string} s
     * @param {number} numRows
     * @return {string}
     */
    convert(s, numRows) {
        if (numRows === 1 || s.length <= numRows) {
            return s
        }

        const rows = Array.from({ length: numRows }, () => '');

        let currentRow = 0;
        let isGoingDown = true;

        for (const char of s) {
            rows[currentRow] += char;

            if (currentRow === 0) {
                isGoingDown = true;
            } else if (currentRow === numRows - 1) {
                isGoingDown = false;
            }

            currentRow += isGoingDown ? 1 : -1;
        }
        return rows.join('')
    }
}
