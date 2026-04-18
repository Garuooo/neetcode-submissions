class Solution:
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


