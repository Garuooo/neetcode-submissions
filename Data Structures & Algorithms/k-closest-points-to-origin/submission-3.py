class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]

        for x,y in points:
            distance = x**2 + y**2
            minheap.append((distance,[x,y]))

        heapq.heapify(minheap)
        res = heapq.nsmallest(k,minheap)
        res = [element[1] for element in res]
        return res