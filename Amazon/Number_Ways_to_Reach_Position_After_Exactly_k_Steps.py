# Runtime = 23ms (99.66%) 
# Memory = 13.8MB (98.63%)

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if (k - abs(endPos - startPos)) % 2 == 1 or k < abs(startPos - endPos):
            return 0
        d1 = (k - abs(endPos - startPos)) // 2
        d2 = k - d1
        res = math.factorial(k) // (math.factorial(d1) * math.factorial(d2)) 
        return res % 1_000_000_007