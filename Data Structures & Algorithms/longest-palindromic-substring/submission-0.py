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