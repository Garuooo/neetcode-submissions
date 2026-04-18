class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def dfs(index,current_sum):
            if index >= len(nums):
                if current_sum== target:
                    return 1
                else:
                    return 0
            
            res = dfs(index+1,current_sum-nums[index]) + dfs(index+1,current_sum+nums[index])
            return res
        return dfs(0,0)