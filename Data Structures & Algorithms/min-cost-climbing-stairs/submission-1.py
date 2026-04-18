class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo={}
        def dfs(index):
            if index >= len(cost):
                return 0
            if index in self.memo:
                return self.memo[index]
            one_steps=dfs(index+1)+cost[index]
            two_steps=dfs(index+2)+cost[index]
            self.memo[index] =  min(one_steps,two_steps)
            return self.memo[index]
        return min(dfs(0),dfs(1))