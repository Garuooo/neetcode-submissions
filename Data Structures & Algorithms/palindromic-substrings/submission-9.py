class Solution:
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



    
                