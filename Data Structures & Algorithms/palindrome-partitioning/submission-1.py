class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,part=[],[]
        

        def isPalindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i,len(s)):
                if isPalindrome(i,j):
                    print(s[i:j+1])
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res



















    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(string):
            l,r=0,len(string)-1
            while l<r:
                if string[l]!=string[r]:
                    return False
                l+=1
                r-=1
            return True
        
        partitions=[]
        res = []
        def dfs(index):
            if index >= len(s):
                res.append(partitions[:])
                return

            for i in range(index,len(s)):
                print(s[index:i+1])
                if isPalindrome(s[index:i+1]):
                    partitions.append(s[index:i+1])
                    dfs(i+1)
                    partitions.pop()

        dfs(0)
        return res
    