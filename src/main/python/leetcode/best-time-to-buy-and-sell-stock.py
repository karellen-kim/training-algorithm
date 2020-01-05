class Solution(object):
    def maxProfit(self, prices):
        if (len(prices) == 0) :
            return 0

        minPrice = prices[0]
        maxProfit = 0
        for price in prices[1:] :
            if price > minPrice :
                maxProfit = max(maxProfit, price - minPrice)
            else :
                minPrice = min(minPrice, price)

        return maxProfit