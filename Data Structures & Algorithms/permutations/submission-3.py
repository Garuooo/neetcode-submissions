class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]
        permutations=[]

        for index in range(len(nums)):
            element = nums[index]
            remaining_elements=nums[:index]+nums[index+1:]

            for p in self.permute(remaining_elements):
                permutations.append([element]+p)
        return permutations





