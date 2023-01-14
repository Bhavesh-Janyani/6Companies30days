# Runtime = 960ms (97.85%) 
# Memory = 22.4MB (77.42%)

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        num = [j for i in matrix for j in i]
        negative = (sum(1 for i in num if i<0))%2 
        num = [abs(i) for i in num] 
        if negative:
            min_ = min(num) 
            return sum(num) - min_*2
        else:
            return sum(num)