class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        def dfs(index):
            if index > len(cost):
                return float('inf')

            if index == len(cost):
                return 0
            
            one_step = cost[index] + dfs(index+1)
            two_step = cost[index] + dfs(index+2)

            return min(one_step,two_step)

        return min(dfs(0),dfs(1))