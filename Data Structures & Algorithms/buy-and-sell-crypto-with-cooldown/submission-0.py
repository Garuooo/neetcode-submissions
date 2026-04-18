class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        def dfs(index,bought,profit):

            if index >= len(prices):
                return profit
            
            if bought:
                sell = dfs(index+2,False,profit+prices[index])
                skip = dfs(index+1,bought,profit)
                return max(sell,skip)

            else:
                buy = dfs(index+1,True,profit-prices[index])
                skip = dfs(index+1,bought,profit)
                return max(buy,skip)
        return dfs(0,False,0)