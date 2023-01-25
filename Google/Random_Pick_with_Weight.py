# Runtime = 694ms (26.24%) 
# Memory = 18.3MB (91.82%)

class Solution:
    def __init__(self, w: List[int]):
        self.s = []
        self.total = 0
        for weight in w:
            self.total+=weight
            self.s.append(self.total)
    def pickIndex(self) -> int:
        rnd = random.randint(1, self.total)
        indx = bisect_left(self.s, rnd)
        return indx