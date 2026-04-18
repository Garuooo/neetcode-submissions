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


    def generateParenthesis(self, n: int) -> List[str]:
        # 1 ( > )
        # 2 ) > (
        self.res=[]
        self.stack=[]
        def backtrack(openings,closings):
            if len(self.stack) == 2*n and openings==closings:
                self.res.append("".join(self.stack))
            
            if len(self.stack) > 2*n:
                return False
            
            if openings > closings:
                self.stack.append(")")
                backtrack(openings,closings+1)
                self.stack.pop()
            
            self.stack.append("(")
            backtrack(openings+1,closings)
            self.stack.pop()

        backtrack(0,0)
        return self.res


