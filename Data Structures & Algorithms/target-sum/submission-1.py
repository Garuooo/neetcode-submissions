class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo={}
        def dfs(index,current_sum):

            if index >= len(nums):
                if current_sum== target:
                    return 1
                else:
                    return 0
            key = str((index,current_sum))
            if key in self.memo:
                return self.memo[key]
                
            self.memo[key] = dfs(index+1,current_sum-nums[index]) + dfs(index+1,current_sum+nums[index])
            return  self.memo[key]
        return dfs(0,0)