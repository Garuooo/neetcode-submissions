class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.res=[]
        self.combination=[]
        self.memo={}
        def dfs(left,right):
            if (left,right) in self.memo:
                return self.memo[(left,right)]
            if left == right == len(s):
                return True
            
            if left > right or right > len(s):
                return False
            shrink=False
            ## branch a new word
            if s[left:right+1] in wordDict:
                shrink = dfs(right+1,right+1)
            ## keep adding
            expand = dfs(left,right+1)
            self.memo[(left,right)] = shrink or expand
            return self.memo[(left,right)]
        return dfs(0,0)