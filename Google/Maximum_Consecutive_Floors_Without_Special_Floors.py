# Runtime = 682ms (96.67%) 
# Memory = 28.2MB (52.78%)

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special = sorted(special)
        lastSpeciaFloor = bottom - 1
        maxConsecutiveFloors = 0
        for floor in special:
            maxConsecutiveFloors = max(maxConsecutiveFloors, floor - lastSpeciaFloor - 1)
            lastSpeciaFloor = floor
        maxConsecutiveFloors = max(maxConsecutiveFloors, top - lastSpeciaFloor)
        return maxConsecutiveFloors