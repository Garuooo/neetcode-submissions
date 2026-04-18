class Solution:






    def subsets(self, nums: List[int]) -> List[List[int]]:

        subset=[]
        res=[]

        def dfs(index):
            if index >= len(nums):
                res.append(subset[:])
                return
            
            #take  
            subset.append(nums[index])
            dfs(index+1)
            #leave
            subset.pop()
            dfs(index+1)

        dfs(0)
        return res

