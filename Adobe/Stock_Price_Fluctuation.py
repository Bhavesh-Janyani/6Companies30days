# Runtime = 1121ms (50.24%) 
# Memory = 56.2MB (86.62%)

from sortedcontainers import SortedDict, SortedList
class StockPrice:
    def __init__(self):
        self.time = SortedDict()
        self.prices = SortedList()
    
    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time.keys():
			#remove old price and add new price
            self.prices.remove(self.time[timestamp])
            self.time[timestamp] = price
            self.prices.add(price)
        else:
			#add new price
            self.time[timestamp] = price
            self.prices.add(price)

    def current(self) -> int:
		#return value of rightmost key
        return self.time[self.time.keys()[-1]]

    def maximum(self) -> int:
		#return rightmost element in prices
        return self.prices[-1]

    def minimum(self) -> int:
		#return leftmost element in prices
        return self.prices[0]
        