class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        stack=[]

        for bracket in s:
            if bracket not in mapping:
                stack.append(bracket)
            else:
                if not stack or stack.pop() != mapping[bracket]:
                    return False
        return not stack