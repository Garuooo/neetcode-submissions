class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2
            n = n >> 1 ## shift n bit by 1 to the right : instead of 10111 it will be 1011
        
        return res