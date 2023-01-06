# Runtime = 3153ms (18.84%) 
# Memory = 15.1MB (91.48%)

class Solution:
    def longestPrefix(self, s: str) -> str:
        res = ''
        for i in range(1, len(s)):
            if s[:i] == s[-i:]:
                res = s[:i]
        return res
