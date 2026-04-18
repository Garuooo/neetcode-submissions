class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        def dfs(index,res,count):
            
            if res > amount:
                return float("inf")

            if index >= len(coins):
                return float("inf")
            
            if res == amount:
                return count
            
            return min(dfs(index,res+coins[index],count+1),dfs(index+1,res,count))

        res = dfs(0,0,0)
        return res if res < float("inf") else -1


    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(res):
            # Check if the result is already computed
            if res in memo:
                return memo[res]
            
            if res == 0:
                return 0
            if res < 0:
                return float("inf")

            # Try each coin and take the minimum result
            min_coins = float("inf")
            for coin in coins:
                count = dfs(res - coin)
                if count != float("inf"):
                    min_coins = min(min_coins, count + 1)
            
            # Store the result in the memo dictionary
            memo[res] = min_coins
            return memo[res]

        res = dfs(amount)
        return res if res != float("inf") else -1