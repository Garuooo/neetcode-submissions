class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for element in s:
            if element in "0123456789" or ord("a") <= ord(element) <= ord("z") or ord("A") <= ord(element) <= ord("Z"):
                new_s.append(element)

        new_s = "".join(new_s).lower()
        left = 0 
        right = len(new_s) - 1
        while left < right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1 
        
        return True