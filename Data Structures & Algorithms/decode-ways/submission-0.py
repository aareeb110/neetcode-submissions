class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        
        prev = 1 # dp[i - 1]
        prev2 = 1 # dp[i - 2]

        for i in range(2, n + 1):
            current = 0
            one_digit = int(s[i - 1 : i])
            two_digit = int(s[i - 2 : i])

            if 1<= one_digit <= 9:
                current += prev
            if 10 <= two_digit <= 26:
                current += prev2
            
            prev2 = prev
            prev = current

        return prev