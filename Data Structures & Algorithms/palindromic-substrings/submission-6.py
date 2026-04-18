class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindorme(i,j):
            left,right=i,j
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True
        substrings=[]
        self.memo={}
        def dfs(index):
            if index >= len(s):
                return []
            for i in range(index,len(s)):
                if isPalindorme(index,i):
                    substrings.append(s[index:i+1])
            dfs(index+1)
        dfs(0)
        return len(substrings)

    
                