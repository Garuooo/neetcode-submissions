class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range(len(nums)-k+1):
            maximum=float("-inf")
            for j in range(k):
                maximum=max(maximum,nums[i+j])
            res.append(maximum)
        return res