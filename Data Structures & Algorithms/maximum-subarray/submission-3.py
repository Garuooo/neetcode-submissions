class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float("-inf")
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                current_sum=sum(nums[i:j+1])
                max_sum=max(current_sum,max_sum)
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        total=0
        max_sum=float("-inf")
        for element in nums:
            total+=element

            max_sum=max(max_sum,total)
            if total < 0:
                total = 0 

        return max_sum

