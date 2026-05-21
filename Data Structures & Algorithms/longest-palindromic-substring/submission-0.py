class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right] # exclude the last left and right
        
        longest_palindrome = ""
        for i in range(len(s)):
            # Odd length palindrome
            palindrome1 = expand_around_center(i, i)
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            
            # Even length
            palindrome1 = expand_around_center(i, i + 1)
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
        return longest_palindrome
