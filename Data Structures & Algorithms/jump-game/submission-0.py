class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(index):
            print(index,nums[index])
            if index >= len(nums)-1:
                return True

            for i in range(index+1,index+nums[index]+1):
                if dfs(i):
                    return True

            return False
        return dfs(0)
