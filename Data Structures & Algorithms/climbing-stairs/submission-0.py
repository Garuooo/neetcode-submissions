class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(step):
            if step == n:
                return 1
            if step > n:
                return 0
            res = dfs(step+1) + dfs(step+2)
            return res
        return dfs(0)