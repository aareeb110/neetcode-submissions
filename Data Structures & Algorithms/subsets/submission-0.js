class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        const result = [];
        const currentSubset = [];

        const backtrack = (index) => {
            result.push([...currentSubset]);
            for (let i = index; i < nums.length; i++) {
                currentSubset.push(nums[i]);
                backtrack(i + 1);
                currentSubset.pop();
            }
        };

        backtrack(0);
        return result;
    }
}
