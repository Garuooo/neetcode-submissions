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


    def isPalindrome(self, s: str) -> bool:
        def is_valid(character):
            if ord("a") <= ord(character) <= ord("z"):
                return True
            
            if ord("A") <= ord(character) <= ord("Z"):
                return True
            
            if character in "0123456789":
                return True
            
            return False
        
        left, right = 0, len(s)-1
        while left < right:
            while left < len(s) and not is_valid(s[left]):
                left += 1
            
            while right > 0 and not is_valid(s[right]):
                right -= 1

            if left < len(s) and right > 0 and s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True