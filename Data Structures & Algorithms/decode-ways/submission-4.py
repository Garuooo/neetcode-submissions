class Solution:
    def numDecodings(self, s: str) -> int:
        self.res = []
        self.combination = []

        if s[0]=="0":
            return 0

        def dfS(index):
            if index >= len(s):
                if len(self.combination) > 0:
                    self.res.append("".join(self.combination.copy()))
                return
            
            # Check if the current digit is valid (1-9)
            if s[index] != "0":
                l = chr(int(s[index]) + 64)
                self.combination.append(l)
                dfS(index + 1)
                self.combination.pop()

            # Check if the next two digits form a valid number (10-26)
            if index + 1 < len(s) and s[index] != "0" and s[index:index + 2] <= "26":
                l = chr(int(s[index:index + 2]) + 64)
                self.combination.append(l)
                dfS(index + 2)
                self.combination.pop()
        
        dfS(0)
        return len(self.res)