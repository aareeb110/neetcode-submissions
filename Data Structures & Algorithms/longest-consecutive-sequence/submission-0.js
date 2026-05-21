class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const numSet = new Set(nums);
        let maxLen = 0;

        for (const num of numSet) {
            if (!numSet.has(num - 1)) {
                let currentNum = num;
                let currentLen = 1;

                while (numSet.has(currentNum + 1)) {
                    currentNum++;
                    currentLen++;
                }

                if (currentLen > maxLen) {
                    maxLen = currentLen;
                }
            }
        }
        return maxLen;
    }
}
