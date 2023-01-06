# Runtime = 2439ms (41.18%) 
# Memory = 20.1MB (96.8%)

class Solution(object):
    def maxRotateFunction(self, A):
        r = curr = sum(i * j for i,j in enumerate(A))
        s = sum(A)
        k = len(A)
        while A:
            curr += s - A.pop() * k
            r = max(curr, r)
        return r
        
# O(N) time
# O(1) space