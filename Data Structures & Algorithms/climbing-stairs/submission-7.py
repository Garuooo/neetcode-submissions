
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
        nums = [1,1]
        for i in range(2,n+1):
            nums.append(nums[i-1]+nums[i-2])
        print(nums)
        return nums[n]