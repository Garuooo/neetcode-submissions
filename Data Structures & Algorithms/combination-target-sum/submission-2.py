class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        combination=[]

        res = []

        def dfs(index,combination):
            if sum(combination)==target:
                res.append(combination[:])
                return 

            if sum(combination)>target:
                return False

            if index >= len(nums):
                return False
            #take
            dfs(index,combination+[nums[index]])
            #leave
            dfs(index+1,combination)

        dfs(0,[])
        return res