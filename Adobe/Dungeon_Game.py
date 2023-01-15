# Runtime = 60ms (62.65%) 
# Memory = 14.4MB (89.16%)

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[m - 1][n - 1] = 1 if dungeon[m - 1][n - 1] >= 0 else abs(dungeon[m - 1][n - 1]) + 1
        for j in range(n - 2, -1, -1):
            if dungeon[m - 1][j] >= 0:
                dp[m - 1][j] = max(1, dp[m - 1][j + 1] - dungeon[m - 1][j])
            else:
                dp[m - 1][j] = abs(dungeon[m - 1][j]) + dp[m - 1][j + 1]
        for i in range(m - 2, -1, -1):
            if dungeon[i][n - 1] >= 0:
                dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])
            else:
                dp[i][n - 1] = abs(dungeon[i][n - 1]) + dp[i + 1][n - 1]
                
            for j in range(n - 2, -1, -1):
                if dungeon[i][j] >= 0:
                    dp[i][j] = min(max(1, dp[i + 1][j] - dungeon[i][j]), max(1, dp[i][j + 1] - dungeon[i][j]))
                else:
                    dp[i][j] = abs(dungeon[i][j]) + min(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]