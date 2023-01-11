# Runtime = 827ms (98.48%) 
# Memory = 27MB (57.58%)

class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False