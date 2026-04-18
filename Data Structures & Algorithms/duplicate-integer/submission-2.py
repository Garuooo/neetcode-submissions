class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #      return not len(list(nums))==len(set(nums))


    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash={}
        for element in nums:
            if element in nums_hash:
                return True
            nums_hash[element]=True
        return False