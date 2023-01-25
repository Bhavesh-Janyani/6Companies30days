# Runtime = 1886ms (5.38%) 
# Memory = 15.8MB (99.39%)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k1: int) -> int:
        dp = [[float('inf')]*n for i in range(n)]
        for i,j,x in times:
            dp[i-1][j-1] = x
        for i in range(n):
            dp[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
        mx = -float('inf')
        for x in range(n):
            i = dp[k1-1][x]
            if(i==float('inf')):
                return -1
            mx = max(i,mx)
        return mx