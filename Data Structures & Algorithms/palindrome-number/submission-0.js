class Solution {
    /**
     * @param {number} x
     * @return {boolean}
     */
    isPalindrome(x) {
        if (x < 0) {
            return false;
        }

        const original = x;
        let rev = 0;

        while (x > 0) {
            const digit = x % 10;
            rev = rev * 10 + digit;
            x = Math.floor(x / 10);
        }
        return rev === original;
    }
}
