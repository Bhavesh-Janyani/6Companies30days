# Runtime = 486ms (37.21%) 
# Memory = 13.8MB (100%)

class Solution(object):
    def numberOfSubstrings(self, s):
        res = i = 0
        count = {c: 0 for c in 'abc'}
        for j in xrange(len(s)):
            count[s[j]] += 1
            while all(count.values()):
                count[s[i]] -= 1
                i += 1
            res += i
        return res