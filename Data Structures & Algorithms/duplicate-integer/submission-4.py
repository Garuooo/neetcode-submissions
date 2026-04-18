class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = []
        for element in nums:
            if element in nums2:
                return True
            nums2.append(element)
        return False