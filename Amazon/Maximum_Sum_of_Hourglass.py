# Runtime = 271ms (88.60%) 
# Memory = 17.1MB (75.40%)

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_hourglass_sum = 0
        for i in range(2,m):
            for j in range(n-2):
                sum1 = sum(grid[i-2][j:j+3]+grid[i-1][j+1:j+2]+grid[i][j:j+3])
                max_hourglass_sum = max(max_hourglass_sum,sum1)
        return max_hourglass_sum
        