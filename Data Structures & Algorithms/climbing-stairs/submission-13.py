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