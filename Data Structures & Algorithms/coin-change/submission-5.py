class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i,amount):
            if (i,amount) in cache:
                return cache[(i,amount)]
            if i >= len(coins):
                return float("inf")
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            take = dfs(i,amount-coins[i]) + 1
            leave = dfs(i+1, amount) 
            cache[(i,amount)] = min(take,leave)
            return cache[(i,amount)]
        res = dfs(0,amount) 
        return res if res < float("inf") else -1