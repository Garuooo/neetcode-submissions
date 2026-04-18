class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)

            if x > y:
                x = x - y
                heapq.heappush(stones,-x)
            
        return -1 * stones[0] if len(stones)==1 else 0