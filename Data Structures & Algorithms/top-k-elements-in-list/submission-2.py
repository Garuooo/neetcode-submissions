class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = [[] for num in nums]
        for element,frequency in counter.items():
            res[frequency-1].append(element)
        result=[]
        for index in range(len(res)-1,-1,-1):
            while res[index] and k:
                result.append(res[index].pop())
                k-=1
        return result
