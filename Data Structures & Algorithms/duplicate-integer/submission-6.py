class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = [1,2,3,4,5,6,7]
        for element in nums:
            if element in nums2:
                return True
            for element2 in nums2:
                if element == element2:
                    return True
            nums2.append(element)
        return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for element in nums:
            if element in hashmap:
                return True
            hashmap[element]=True
        return False