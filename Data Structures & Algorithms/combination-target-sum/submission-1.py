class Solution:
    # def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
    #     res=[]
    #     def dfs(index,combination):

    #         if index >= len(nums):
    #             return 
            
    #         if sum(combination) == target:
    #             if combination not in res:
    #                 res.append(combination)
            
    #         if sum(combination) > target:
    #             return
    #         # take
    #         dfs(index,combination+[nums[index]])
    #         # leave
    #         dfs(index+1,combination)
        
    #     dfs(0,[])
    #     return res


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        comb=[]
        def dfs(index):
            print(comb,res)
            if index >= len(nums):
                return
            if sum(comb) == target:
                res.append(comb[:])
                return
            if sum(comb) > target:
                return
            comb.append(nums[index])
            dfs(index)

            comb.pop()
            dfs(index+1)

        dfs(0)
        print(res,"tt")
        return res
