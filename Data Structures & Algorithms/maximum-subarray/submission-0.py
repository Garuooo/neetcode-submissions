class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=0
        max_sum=float("-inf")
        for element in nums:
            total+=element

            max_sum=max(max_sum,total)
            if total < 0:
                total = 0 

        return max_sum