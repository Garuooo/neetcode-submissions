class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def dfs(index,current_steps):
            # if index in self.memo:
            #     return self.memo[index]

            if index>=len(nums)-1:
                # self.memo[index]=True
                # return self.memo[index]
                return current_steps
            min_steps=float("inf")
            for i in range(nums[index],0,-1):
                min_steps = min(dfs(i+index,current_steps+1),min_steps)
            
            return min_steps
        return dfs(0,0)
        
