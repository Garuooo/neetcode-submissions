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


    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        nums[-2] = max(nums[-1],nums[-2])
        for i in range(len(nums)-3,-1,-1):
            nums[i] = max(nums[i]+nums[i+2],nums[i+1])
        return nums[0]