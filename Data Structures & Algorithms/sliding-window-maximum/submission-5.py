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
        deq = deque()
        maximum=0
        index = 0
        while index < len(nums)+1:
            print(deq)
            while len(deq)<k:
                deq.append(nums[index])
                index+=1
                continue
            if len(deq)==k:
                res.append(max(deq))
                deq.popleft()
            if index < len(nums):
                deq.append(nums[index])
                index+=1
            else:
                break
        return res