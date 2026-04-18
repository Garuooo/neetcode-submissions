class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(index,nums1,nums2):
            if index >= len(nums):
                return sum(nums1)==sum(nums2)

            return (dfs(index+1,nums1+[nums[index]],nums2) or
            dfs(index+1,nums1,nums2+[nums[index]]))   
             
        return dfs(0,[],[])

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(index,s1,s2):
            if index >= len(nums):
                return s1==s2

            return (dfs(index+1,s1+nums[index],s2) or
            dfs(index+1,s1,s2+nums[index]))   
             
        return dfs(0,0,0)