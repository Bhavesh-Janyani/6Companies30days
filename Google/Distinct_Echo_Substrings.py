# Runtime = 2105ms (77.1%) 
# Memory = 14.5MB (73.56%)

class Solution:
    def distinctEchoSubstrings(self, s: str) -> int:
        some_strings = set()
        for j in range(len(s)):
            for i in range(j):
                if s.startswith(s[i:j], j):
                    some_strings.add(s[i:j])
        return len(some_strings)