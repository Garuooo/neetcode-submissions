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
        def backtrack(s,openings,closings):
            if len(s) == 2*n and openings==closings:
                self.res.append(s)
            
            if len(s) > 2*n:
                return False
            
            if openings > closings:
                backtrack(s+")",openings,closings+1)
            backtrack(s+"(",openings+1,closings)

        backtrack("",0,0)
        return self.res


