class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        profit=0
        for price in prices:        
            profit = max(profit,price-lowest)
            if lowest > price:
                lowest=price
        
        return profit
        #          *
        #     * 
        #    *  
        #   *
        #       *
        #
        