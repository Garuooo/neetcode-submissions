
class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo={}
        def dfs(step):
            if step == n:
                return 1
            if step > n:
                return 0
            if step in self.memo:
                return self.memo[step]
            self.memo[step] = dfs(step+1) + dfs(step+2)
            return self.memo[step]
        return dfs(0)