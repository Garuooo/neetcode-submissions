class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        heapq.heapify(nums)
        output = 1
        while nums:
            element = heapq.heappop(nums)
            if element > 0:
                if output != element:
                    return output
                output += 1
        
        return output