class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
        def dfs(index,combination):

            if index >= len(nums):
                return 
            
            if sum(combination) == target:
                if combination not in res:
                    res.append(combination)
            
            if sum(combination) > target:
                return
            # take
            dfs(index,combination+[nums[index]])
            # leave
            dfs(index+1,combination)
        
        dfs(0,[])
        return res

