
class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo={}
        def dfs(num):
            if num in self.memo:
                return self.memo[num]
            if num > n:
                return 0
            if num == n:
                return 1
            self.memo[num] = dfs(num+1) + dfs(num+2)
            return self.memo[num] 
        return dfs(0)

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        n1=1
        n2=1
        for n in range(2,n+1):
            temp = n1+n2
            n1=n2
            n2=temp
        return temp