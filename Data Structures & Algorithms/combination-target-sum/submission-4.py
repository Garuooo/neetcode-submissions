class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        def dfs(i,current_sum):
            if i == len(nums):
                if current_sum == target:
                    res.append(combination.copy())
                return
            if current_sum > target:
                return
            combination.append(nums[i])
            current_sum += nums[i]
            dfs(i,current_sum)

            combination.pop()
            current_sum -= nums[i]
            dfs(i+1,current_sum)
        
        dfs(0,0)
        return res