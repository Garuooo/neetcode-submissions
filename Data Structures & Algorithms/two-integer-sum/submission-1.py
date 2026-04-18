class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}
        for index,element in enumerate(nums):
            target_element = target-element
            if target_element in elements:
                return [elements[target_element],index]
            elements[element]=index
        return -1