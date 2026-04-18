class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         return not len(list(nums))==len(set(nums))