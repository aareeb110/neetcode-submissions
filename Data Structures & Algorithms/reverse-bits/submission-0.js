class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number} - a positive integer
     */
    reverseBits(n) {
        let result = 0;
        for (let i = 0; i < 32; i++) {
            const bit = (n >> i) & 1;
            result = result | (bit << (31 - i));
        }
        return result >>> 0;
    }
}
