class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets=["}","]",")"]
        opening_brackets=["(","[","{"]
        mapping={
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack=[]
        for character in s:
            if character in opening_brackets:
                stack.append(character)
            else:
                if not stack or mapping[character] != stack.pop():
                    return False
        return True and not stack