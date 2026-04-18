class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo={}
        def dfs(index):
            if index >= len(nums):
                return 0
            if index in self.memo:
                return self.memo[index]
            leave = dfs(index+1)
            steal = dfs(index+2) + nums[index]
            self.memo[index] = max(leave,steal)
            return self.memo[index]
        return dfs(0)