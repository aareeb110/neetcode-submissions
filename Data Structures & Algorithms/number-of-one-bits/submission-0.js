class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number}
     */
    hammingWeight(n) {
            let count = 0;
    while (n > 0) {
        if ((n & 1) == 1) {
            count++;
        }
        n = n >> 1; // same as n / 2
    }
    return count;
    }
}