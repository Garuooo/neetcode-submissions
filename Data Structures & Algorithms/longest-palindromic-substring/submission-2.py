class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def isPalindrome(string):
            l,r=0,len(string)-1
            while l<r:
                if string[l] != string[r]:
                    return False
                l+=1
                r-=1
            return True
        self.res=""
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                new_string=s[i:j+1]
                if isPalindrome(new_string):
                    if len(self.res) < len(new_string):
                        self.res=new_string
        return self.res


    def longestPalindrome(self, s: str) -> str:
        res=""
        # odd palindromes
        for i in range(len(s)):
            l,r=i,i
            while r < len(s) and l >= 0 and s[l]==s[r]:
                if (r-l+1) > len(res):
                    res=s[l:r+1]
                l-=1
                r+=1

            l,r=i,i+1
            while l >=0 and r < len(s) and s[l]==s[r]:
                if len(res) < (r-l+1):
                    res=s[l:r+1]
                l-=1
                r+=1
        return res