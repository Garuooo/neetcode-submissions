class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            
            one_step = dfs(i+1) + cost[i]
            two_step = dfs(i+2) + cost[i]
            cache[i] = min(one_step,two_step)
            return cache[i]
        return min(dfs(0),dfs(1))
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        for n in range(len(cost)-3,-1,-1):
            cost[n] = min(cost[n+1], cost[n+2]) + cost[n]
        return min(cost[0],cost[1])