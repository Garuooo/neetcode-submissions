class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        self.subarrays=[]
        def dfs(left,right,subarray):
            
            if left >= len(heights) or right >= len(heights) or left > right:
                self.subarrays.append(min(subarray)*len(subarray))
                return
            if subarray:
                self.subarrays.append(min(subarray)*len(subarray))
            
            #add
            dfs(left,right+1,subarray+[heights[right]])

            #shrink
            t = subarray[:]
            if t:
                t.pop(0)
                dfs(left+1,right,t)
        dfs(0,0,[])
        return max(self.subarrays)
