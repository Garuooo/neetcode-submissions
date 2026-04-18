class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters=[]
        for letter in s:
            if ord("a") <= ord(letter) <= ord("z"):
                letters.append(letter)
            if ord("A") <= ord(letter) <= ord("Z"):
                letters.append(letter.lower())
            if ord("0") <= ord(letter) <= ord("9"):
                letters.append(letter)
        
        left,right=0,len(letters)-1

        while left < right:
            if letters[left]!=letters[right]:
                return False
            left+=1
            right-=1
        return True