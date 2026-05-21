class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        if (nums.length === 1) {
            return nums[0];
        }

        let rob = nums[0];
        let notRob = 0;

        for (let i = 1; i < nums.length; i++) {
            let newRob = notRob + nums[i];
            let newNotRob = Math.max(rob, notRob);

            rob = newRob;
            notRob = newNotRob;
        }

        return Math.max(rob, notRob);
    }
}
