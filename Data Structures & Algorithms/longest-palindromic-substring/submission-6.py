class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        if len(s) == 2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        x = ""
        for i in range(len(s)):
            # odd palindromes
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left]==s[right]:
                if len(x)<right-left+1:
                    x=s[left:right+1]
                left -=1
                right +=1
            left = i - 1
            right = i
            while left >= 0 and right < len(s) and s[left]==s[right]:
                if len(x)<right-left+1:
                    x=s[left:right+1]
                left -=1
                right +=1
        return x