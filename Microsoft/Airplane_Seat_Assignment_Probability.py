# Runtime = 19ms (64.86%) 
# Memory = 13.3MB (97.30%)

class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        return (1 if n == 1 else 0.5)