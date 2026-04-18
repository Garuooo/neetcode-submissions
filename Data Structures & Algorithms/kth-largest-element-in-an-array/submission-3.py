class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-n for n in nums]
        heapq.heapify(nums)
        res = []
        while len(res) < k:
            res.append(-1 * (heapq.heappop(nums)))
        return res[k-1]