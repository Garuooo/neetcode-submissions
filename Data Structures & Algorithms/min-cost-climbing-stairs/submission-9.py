from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i >= len(cost):
                return 0

            return min(
                dfs(i+1),
                dfs(i+2) 
            ) + cost[i]

        return min(dfs(0),dfs(1))


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost)+1)]

        for i in range(2,len(cost)+1):
            dp[i] = min(
                dp[i-1] + cost[i-1],
                dp[i-2] + cost[i-2]
            )
        
        return dp[len(cost)]