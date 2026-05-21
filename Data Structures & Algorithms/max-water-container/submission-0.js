class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let left = 0;
        let right = heights.length - 1;
        let max = 0;

        while (left < right) {
            const width = right - left;
            const h = Math.min(heights[left], heights[right]);

            const currArea = h * width;
            if (currArea > max) {
                max = currArea;
            }

            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return max;
    }
}
