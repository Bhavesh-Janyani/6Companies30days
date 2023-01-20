# Runtime = 246ms (99.81%) 
# Memory = 17.9MB (99.42%)

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = 0
        full = 1 << k
        mask = full - 1
        buff = bytearray(full)
        v = int(s[:k-1], 2) if k > 1 else 0
        for c in s[k-1:]:
          v = ((v << 1) | (c == '1')) & mask
          if not buff[v]:
            seen += 1
            if seen == full:
              return True
            buff[v] = 1
        return False
          