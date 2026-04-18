class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo={}
        if len(nums)==1:
            return nums[0]
        def dfs(houses,index):
            if index >= len(houses):
                return 0
            if index in self.memo:
                return self.memo[index]
            leave = dfs(houses,index+1)
            steal = dfs(houses,index+2) + houses[index]
            self.memo[index] = max(leave,steal)
            return self.memo[index]
        array2=nums[::-1]
        r1 = dfs(nums[:len(nums)-1],0)
        self.memo={}
        r2 = dfs(array2[:len(nums)-1],0)
        return max(r1,r2)