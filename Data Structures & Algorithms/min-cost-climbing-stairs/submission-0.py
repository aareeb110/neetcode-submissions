class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # def solve(i):
        #     if i >= len(cost): return 0
        #     return cost[i] + min(solve(i + 1), solve(i + 2))   
        # return min(solve(0), solve(1)) 
        n = len(cost)
        down_one = 0 # Cost to reach one step below the top
        down_two = 0 # Cost to reach two steps below the top

        for i in range(2, n + 1):
            temp = down_one
            down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
            down_two = temp
        return down_one
