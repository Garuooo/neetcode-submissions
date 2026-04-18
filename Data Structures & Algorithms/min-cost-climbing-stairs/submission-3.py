class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        self.memo={}
        def dfs(index):
            if index in self.memo:
                return self.memo[index]
            if index > len(cost):
                return float('inf')

            if index == len(cost):
                return 0
            
            one_step = cost[index] + dfs(index+1)
            two_step = cost[index] + dfs(index+2)
            self.memo[index] = min(one_step,two_step)
            return self.memo[index]
        return min(dfs(0),dfs(1))