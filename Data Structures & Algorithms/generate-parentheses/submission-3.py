class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Valid Parenthesis will be
        # ()x , x(), (x)
        self.permutations=[]
        self.permutations.append("()")
        def backtrack(n):
            print(self.permutations)
            if n == 0:
                return
            perm=[]
            while self.permutations:            
                element = self.permutations.pop()
                perm.append(f"({element})")
                perm.append(f"(){element}")
                perm.append(f"{element}()")

            self.permutations=perm
            backtrack(n-1)
        backtrack(n-1)
        return list(set(self.permutations))
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        result = []
        backtrack()
        return result
