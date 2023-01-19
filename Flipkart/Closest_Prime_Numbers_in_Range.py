# Runtime = 51ms (84.87%) 
# Memory = 13.8MB (93.88%)

import math

def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for divisor in range(2, math.floor(math.sqrt(num)) + 1):
        if num % divisor == 0:
            return False
    return True


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        primes = []
        for candidate in range(left, right + 1):
            if is_prime(candidate):
                if primes and candidate <= primes[-1] + 2:
                    return [primes[-1], candidate]  # twin or [2, 3]
                primes.append(candidate)
        
        gaps = ([primes[i - 1], primes[i]]
                for i in range(1, len(primes)))

        return min(gaps,
                   key=lambda gap: (gap[1] - gap[0], gap[0]),
                   default=[-1, -1])