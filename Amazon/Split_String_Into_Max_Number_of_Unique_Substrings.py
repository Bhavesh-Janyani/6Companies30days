# Runtime = 51ms (100%) 
# Memory = 13.5MB (86.36%)

class Solution(object):
    def maxUniqueSplit(self, s):
        seen = set()
        def dfs(s, seen):
            if not s:
                return 0
            res = 0
            for i in range(1, len(s) + 1):
                if s[:i] not in seen and len(s) - i + 1 > res:
                    seen.add(s[:i])
                    res = max(res, 1 + dfs(s[i:], seen))
                    seen.remove(s[:i])
            return res
        return dfs(s, seen)