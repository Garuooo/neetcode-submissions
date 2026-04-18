class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap,self.k = nums,k
        heapq.heapify(self.minheap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        print(self.minheap)
        n_largest=heapq.nlargest(self.k,self.minheap)
        print(n_largest)
        return n_largest[-1]