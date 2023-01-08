# Runtime = 833ms (95.94%) 
# Memory = 33.8MB (36.68%)

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minPick = float('inf')
        seen = {}
        for i, n in enumerate(cards):
            if n in seen:
                if i - seen[n] + 1 < minPick:
                    minPick = i - seen[n] + 1
            seen[n] = i
        if minPick == float('inf'):
            return -1
        return minPick