# Runtime = 66ms (97.20%) 
# Memory = 14.3MB (84.62%)

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or N >= K + W:
            return 1
        dp = [1] + [0] * N
        res = 0
        wsum = 1.0
        for i in range(1, N+1):
            dp[i] = wsum / W
            if i < K:
                wsum += dp[i]
            else:
                res += dp[i]
                
            if i - W >= 0:
                wsum -= dp[i-W]
        return res