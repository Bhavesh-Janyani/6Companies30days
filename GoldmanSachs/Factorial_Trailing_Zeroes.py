# Runtime = 12ms (96.51%) 
# Memory = 13.4MB (76.74%)

class Solution(object):
    def trailingZeroes(self, n):
        y =  0
        while n:
            n /= 5
            y += n
        return y