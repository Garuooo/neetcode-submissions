class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash={}
        for index,element in enumerate(nums):
            target_diff=target-element
            if target_diff in nums_hash:
                return [nums_hash[target_diff],index]
            else:
                nums_hash[element]=index