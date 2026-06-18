class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }

        result = []
        def dfs(index, current_combination):
            if (index == len(digits)):
                result.append(current_combination)
                return
            
            digit = digits[index]
            letters = phone_map[digit]

            for letter in letters:
                dfs(index + 1, current_combination + letter)
        
        dfs(0, "")
        return result
        
        