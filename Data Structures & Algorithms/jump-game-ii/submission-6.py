class Solution:
    def jump(self, nums: List[int]) -> int:
        self.memo={}
        def dfs(index):
            print(self.memo)
            if index in self.memo:
                return self.memo[index]

            if index>=len(nums)-1:
                return 0

            min_steps=float("inf")
            for i in range(nums[index],0,-1):
                min_steps = min(dfs(i+index)+1,min_steps)
                self.memo[index]=min_steps
            return min_steps
        return dfs(0)
        
