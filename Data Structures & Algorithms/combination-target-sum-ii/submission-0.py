class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        combination=[]

        def dfs(index,current_sum):
            if current_sum ==target:
                res.append(combination[:])
                return

            if index >= len(candidates):
                return
            
            #take
            combination.append(candidates[index])
            dfs(index+1,current_sum+candidates[index])

            while index+1 < len(candidates) and candidates[index]==candidates[index+1]:
                index+=1
            #leave
            combination.pop()
            dfs(index+1,current_sum)
        dfs(0,0)
        return res