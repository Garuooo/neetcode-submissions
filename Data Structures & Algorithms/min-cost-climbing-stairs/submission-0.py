class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(index):
            if index >= len(cost):
                return 0
            one_steps=dfs(index+1)+cost[index]
            two_steps=dfs(index+2)+cost[index]
            return min(one_steps,two_steps)
        
        return min(dfs(0),dfs(1))