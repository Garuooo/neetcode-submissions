class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            x = x * -1
            y = y * -1
            if x == y:
                continue
            elif x > y:
                heapq.heappush(stones,(x-y)*-1)
            else:
                heapq.heappush(stones,(y-x)*-1)
        if stones:
            return stones[0] * -1
        else:
            return 0



