class Solution:
    def is_palindrome(self, sub: str) -> bool:
        return sub == sub[::-1]
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)

        def dfs(start_index, current_partition):
            if start_index == n:
                result.append(list(current_partition))
                return
            
            for end_index in range(start_index, n):
                substring = s[start_index : end_index + 1]
                if self.is_palindrome(substring):
                    current_partition.append(substring)
                    dfs(end_index + 1, current_partition)
                    current_partition.pop()
        

        dfs(0, [])
        return result