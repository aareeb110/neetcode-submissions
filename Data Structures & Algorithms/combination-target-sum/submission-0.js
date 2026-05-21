class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        const res = [];
        nums.sort((a, b) => a - b);

        const backtrack = (combination, remaining, start) => {
            if (remaining === 0) {
                res.push([...combination]);
                return;
            }

            if (remaining < 0) {
                return;
            }

            for (let i = start; i < nums.length; i++) {
                combination.push(nums[i]);
                backtrack(combination, remaining - nums[i], i);
                combination.pop();
            }
        };

        backtrack([], target, 0);
        return res;
    }
}
