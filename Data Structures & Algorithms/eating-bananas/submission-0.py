class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eat(speed):
            hours=0
            for element in piles:
                hours+=math.ceil(element / speed)
            
            return hours <= h
        
        low,high=1,max(piles)

        res=float("inf")
        while low <= high:
            mid = (low+high)//2
            if eat(mid):
                res=min(res,mid)
                high=mid-1
            else:
                low=mid+1
        
        return res