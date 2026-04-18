class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        stack = []
        for element in s:
            if element in brackets:
                if not stack or stack.pop() != brackets[element]:
                    return False
            else:
                stack.append(element)

        return not stack