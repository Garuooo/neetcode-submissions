class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping={
            "1":"",
            "2":"ABC",
            "3":"DEF",
            "4":"GHI",
            "5":"JKL",
            "6":"MNO",
            "7":"PQRS",
            "8":"TUV",
            "9":"WXYZ",
            "0":"+",
            "*":"*",
            "#":"#"
        }
        res=[]
        def dfs(index,word):
            print(index,word)
            if int(index) >= len(digits):
                if word:
                    res.append(word[:].lower())
                return
            for element in mapping[str(digits[int(index)])]:
                dfs(str(int(index)+1),word+element)
        dfs(str(0),"")
        return res
        print(digits)