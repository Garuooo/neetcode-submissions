class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        comb=[]
        def backtrack(index):
            if index==len(nums) and comb not in res:
                
                res.append(comb[:])
            for i in range(index,len(nums)):
                ## take
                comb.append(nums[i])
                backtrack(i+1)

                ## leave
                comb.pop()
                backtrack(i+1)
        backtrack(0)
        return res