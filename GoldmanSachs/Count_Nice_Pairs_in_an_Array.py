# Runtime = 736ms (78.13%) 
# Memory = 23.1MB (75%)

class Solution(object):
    def countNicePairs(self, A):
        res = 0
        count = collections.Counter()
        for a in A:
            b = int(str(a)[::-1])
            res += count[a - b]
            count[a - b] += 1
        return res % (10**9 + 7)