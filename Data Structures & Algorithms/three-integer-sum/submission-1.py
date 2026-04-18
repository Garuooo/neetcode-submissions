class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def getTargetSum(nums,target):
            left,right=0,len(nums)-1
            lists=[]
            while left<right:
                if nums[left]+nums[right]<target:
                    left+=1
                elif nums[left]+nums[right]>target:
                    right-=1
                elif  nums[left]+nums[right]==target:
                    lists.append([nums[left],nums[right]])
                    left+=1
                    right-=1
            return lists

        for index,element in enumerate(nums):
            target=0-element
            nums_copy=nums[:]
            nums_copy.pop(index)
            val = getTargetSum(nums_copy,target)
            if val:
                for lista in val:
                    if sorted([element,lista[0],lista[1]]) not in res:
                        res.append(sorted([element,lista[0],lista[1]]))
        return res