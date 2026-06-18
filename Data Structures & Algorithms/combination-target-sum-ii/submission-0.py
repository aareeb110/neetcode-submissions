class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(start_index, current_sum, current_combination):
            if current_sum == target:
                results.append(list(current_combination))
                return
            if current_sum > target:
                return
            
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                current_combination.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], current_combination)
                current_combination.pop()
        
        backtrack(0, 0, [])
        return results