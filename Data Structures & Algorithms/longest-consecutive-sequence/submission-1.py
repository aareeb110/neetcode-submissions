class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        ans_len = 0
        for n in nums:
            curr_len = 1
            if n - 1 not in hashset:
                i = n
                while i + 1 in hashset:
                    curr_len += 1
                    i += 1
                if curr_len > ans_len:
                    ans_len = curr_len
        return ans_len