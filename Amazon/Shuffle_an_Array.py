# Runtime = 119ms (90.54%) 
# Memory = 17.5MB (25.23%)

import random
class Solution(object):
    def __init__(self, nums):
        self.nums = nums
        self.original = list(nums)

    def reset(self):
        return self.original

    def shuffle(self):
        aux = self.nums
        random.shuffle(aux)
        return aux