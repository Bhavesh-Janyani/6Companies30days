# Runtime = 120ms (90.91%) 
# Memory = 14.3MB (54.55%)

class Solution(object):
    def getLastMoment(self, n, left, right):
        if len(left) == 0:
            return n - min(right)
        if len(right) == 0:
            return max(left)
        
        return max([n - min(right), max(left)])