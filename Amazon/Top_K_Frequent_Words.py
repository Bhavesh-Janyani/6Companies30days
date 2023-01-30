# Runtime = 54ms (93.12%) 
# Memory = 13.9MB (93.42%)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for x in words:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        res = sorted(dict, key=lambda x: (-dict[x], x))
        return res[:k]