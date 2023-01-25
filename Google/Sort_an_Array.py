# Runtime = 1229ms (86.89%) 
# Memory = 27.8MB (11.11%)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counterNums = Counter(nums)
        minNums = min(nums)
        maxNums = max(nums)
        res = []
        for i in range(minNums, maxNums+1):
            res.extend([i] * counterNums[i])
        
        return res
