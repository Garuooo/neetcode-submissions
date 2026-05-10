from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i):
            nonlocal n 
            if i > n:
                return 0
            if n == i:
                return 1
            
            return dfs(i+1) + dfs(i+2)
        
        return dfs(0)


    def climbStairs(self, n: int) -> int:
        res = [0 for i in range(n+1)]
        res[n] = 1
        res[n-1] = 1
        for i in range(n-2,-1,-1):
            res[i] = res[i+1] + res[i+2]
        
        return res[0]