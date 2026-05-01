class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        combination = []
        def backtrack(i):
            if i == len(nums):
                res.append(combination.copy())
                return
            
                ## take
            combination.append(nums[i])
            backtrack(i+1)
            combination.pop()
            backtrack(i+1)
        backtrack(0)
        return res