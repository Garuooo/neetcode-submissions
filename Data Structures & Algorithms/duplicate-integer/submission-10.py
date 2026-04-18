class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for element in nums:
            if element in hashset:
                return True
            hashset.add(element)
        return False