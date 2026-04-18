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


    def countSubstrings(self, s: str) -> int:

        res = 0

        def countPalindromes(s,l,r):
            palindroms=0
            while l >= 0 and r < len(s) and s[l]==s[r]:
                r+=1
                l-=1
                palindroms+=1
            return palindroms

        for i in range(len(s)):
            res += countPalindromes(s,i,i)
            res += countPalindromes(s,i,i+1)
        return res



    
                