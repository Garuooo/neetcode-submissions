class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range(len(nums)-k+1):
            maximum=float("-inf")
            for j in range(k):
                maximum=max(maximum,nums[i+j])
            res.append(maximum)
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[] 
        deq = nums[:k]
        maximum=0
        index = k
        while index < len(nums)+1:
            if len(deq)==k:
                res.append(max(deq))
                deq.pop(0)
            if index < len(nums):
                deq.append(nums[index])
                index+=1
            else:
                break
        return res