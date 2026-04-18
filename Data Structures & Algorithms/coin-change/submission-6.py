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

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+99 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount] != amount+99 else -1