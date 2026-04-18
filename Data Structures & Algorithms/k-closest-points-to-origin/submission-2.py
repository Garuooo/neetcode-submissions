class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]

        for x,y in points:
            distance = x**2 + y**2
            minheap.append((distance,[x,y]))
        res=[]
        heapq.heapify(minheap)
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res