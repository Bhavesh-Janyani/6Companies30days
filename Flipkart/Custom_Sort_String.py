# Runtime = 27ms (93.97%) 
# Memory = 13.8MB (62.94%)

class Solution:
    def customSortString(self, order: str, T: str) -> str:
        cnt = Counter(T)                            
        ans = [cnt.pop(c, 0) * c for c in order]
        for c, v in cnt.items():
            ans.append(c * v)                       
        return ''.join(ans)