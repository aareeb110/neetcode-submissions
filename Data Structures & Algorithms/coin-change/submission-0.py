class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # base case: 0 coins needed to make up amount 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
            
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]