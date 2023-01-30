# Runtime = 1070ms (98.97%) 
# Memory = 27.8MB (74.42%)

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for astMass in asteroids:
            if astMass <= mass: 
                mass += astMass
            else:
                return False
        return True