class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo={}
        def dfs(row,column):
            print(row,column)
            key=str((row,column))
            if key in self.memo:
                return self.memo[key]
            if row == m and column == n:
                return 1
            if row > m or row < 0 or column > n or column <0:
                return 0
            self.memo[key]= dfs(row+1,column) + dfs(row,column+1)
            return self.memo[key]

        return dfs(1,1)
