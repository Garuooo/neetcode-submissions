class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        subset=[]
        def dfs(index):
            if index >= len(nums):
                if subset not in res:
                    res.append(subset[:])
                return
            

            subset.append(nums[index])
            dfs(index+1)
            subset.pop()
            dfs(index+1)
        dfs(0)
        return res


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        subset=[]
        def dfs(index):
            if index >= len(nums):
                res.append(subset[:])
                return

            subset.append(nums[index])
            dfs(index+1)
            while index+1 < len(nums) and nums[index]==nums[index+1]:
                index+=1
            subset.pop()
            dfs(index+1)
        dfs(0)
        return res