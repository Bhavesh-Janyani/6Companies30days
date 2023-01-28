# Runtime = 129ms (62.80%) 
# Memory = 14.5MB (97.81%)

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float('inf')] * n
        prices[src] = 0        
        for i in range(k + 1):
            temp_prices = list(prices)
            for source, dest, price in flights:
                current_cheapest = temp_prices[dest]
                new_price = prices[source] + price
                if new_price < current_cheapest:
                    temp_prices[dest] = new_price
            prices = temp_prices
        return prices[dst] if prices[dst] != float('inf') else -1