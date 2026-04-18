class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap,self.k = nums,k
        heapq.heapify(self.minheap)


    def add(self, val: int) -> int:
        print(self.minheap,val)
        heapq.heappush(self.minheap,val)
        n_largest=heapq.nlargest(self.k,self.minheap)
        self.minheap=n_largest
        heapq.heapify(self.minheap)
        return n_largest[0]