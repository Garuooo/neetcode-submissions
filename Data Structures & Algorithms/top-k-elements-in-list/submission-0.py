class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_hash={}
        freq = [[] for i in range(len(nums)+1)]
        for element in nums:
            nums_hash[element]=nums_hash.get(element,0) + 1
        for key,value in nums_hash.items():
            print(key,value)
            freq[value].append(key)       

        res=[]

        while k:
            for i in range(len(nums),-1,-1):
                while freq[i] and k>0:
                    res.append(freq[i].pop())
                    k-=1
        return res