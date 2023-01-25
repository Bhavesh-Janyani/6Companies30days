# Runtime = 2648ms (5.9%) 
# Memory = 22.9MB (100%)

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        while True:
            current = len(piles)-2
            if len(piles) < 3:
                break
            else:
                total+=piles[current]
                piles.pop()
                piles.pop()
                piles.remove(piles[0])
        return total
            