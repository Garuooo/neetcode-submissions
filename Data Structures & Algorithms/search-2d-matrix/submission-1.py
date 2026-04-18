class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        



        def binary_search(nums,target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return False

        top=0
        bottom=len(matrix)-1

        while top <= bottom:
            mid = (top+bottom)//2
            if matrix[mid][-1] < target:
                top = mid + 1
            else:
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    if binary_search(matrix[mid],target):
                        return True
                bottom=mid-1
        return False