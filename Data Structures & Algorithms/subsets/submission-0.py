class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(index,subset):
            if index >=len(nums):
                res.append(subset[:])
                return
            #leave
            dfs(index+1,subset)
                #tacke
            dfs(index+1,subset+[nums[index]])
        dfs(0,[])
        return res