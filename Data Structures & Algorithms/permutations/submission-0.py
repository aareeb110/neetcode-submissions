class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(current_perm):
            if len(current_perm) == n:
                result.append(current_perm[:])
                return
            
            for num in nums:
                if num not in current_perm:
                    current_perm.append(num)
                    backtrack(current_perm)
                    current_perm.pop()
        backtrack([])
        return result