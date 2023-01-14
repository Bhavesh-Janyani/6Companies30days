# Runtime = 30ms (89.62%) 
# Memory = 13.8MB (88.45%)

from collections import deque
from itertools import product
from typing import List
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        n, bank = len(start), set(bank)
        q = deque([(start, 0)])
        while q:
            cur, level = q.popleft()
            for i, g in product(range(n), 'ACGT'):
                mutation = cur[:i] + g + cur[i + 1:]
                if mutation in bank:  # unvisited
                    if mutation == end:
                        return level + 1
                    bank.remove(mutation)
                    q.append((mutation, level + 1))
        return -1