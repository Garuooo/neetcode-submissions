class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            steal = dfs(i+2) + nums[i]
            no_steal = dfs(i+1) 
            cache[i] =  max(steal,no_steal)
            return cache[i] 
        return dfs(0)