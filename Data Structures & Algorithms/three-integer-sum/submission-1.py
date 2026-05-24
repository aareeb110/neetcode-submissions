class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sort_nums = sorted(nums)
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            if i > 0 and sort_nums[i] == sort_nums[i - 1]:
                continue
            while left < right:
                if sort_nums[i] + sort_nums[left] + sort_nums[right] > 0:
                    right -= 1
                elif sort_nums[i] + sort_nums[left] + sort_nums[right] < 0:
                    left += 1
                else:
                    ans.append([sort_nums[i], sort_nums[left], sort_nums[right]])
                    left += 1
                    right -= 1
                    # advance past left duplicates
                    while left < right and sort_nums[left] == sort_nums[left - 1]:
                        left += 1
        return ans
