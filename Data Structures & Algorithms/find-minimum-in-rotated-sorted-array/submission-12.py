class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        left,right=0,len(nums)-1
        minimum = float("inf")

        while left <= right:
            mid = (left+right)//2
            print(left,right,mid)
            minimum = min(minimum,nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return minimum


















    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        minimum=float("inf")
        while left <= right:
            mid=(left+right)//2
            minimum=min(minimum,nums[mid])
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid-1
            
        return minimum
