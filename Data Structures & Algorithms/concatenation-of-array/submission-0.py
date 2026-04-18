class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in nums.copy():
            nums.append(i)
        return nums