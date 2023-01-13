# Runtime = 31ms (93.66%) 
# Memory = 13.9MB (30.28%)

class Solution(object):
    def findIntegers(self, num):
        x, y = 1, 2
        res = 0
        num += 1
        while num:
            if num & 1 and num & 2:
                res = 0
            res += x * (num & 1)
            num >>= 1
            x, y = y, x + y
        return res