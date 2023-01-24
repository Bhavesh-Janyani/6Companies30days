# Runtime = 81ms (95.71%) 
# Memory = 14.2MB (40%)

class Solution(object):
    def swimInWater(self, grid):
        b = grid[0][0]
        m, n = len(grid), len(grid[0])
        g = grid
        s = [(g[0][0], 0, 0)]
        visit = {(0,0):1}
        while s:
            v, i, j = heapq.heappop(s)
            b = max(b, v)
            if i==m-1 and j==n-1:
                return b
            if i+1<m and (i+1,j) not in visit:
                visit[(i+1, j)] = 1
                heapq.heappush(s, (g[i+1][j], i+1, j))
            if j+1<n and (i,j+1) not in visit:
                heapq.heappush(s, (g[i][j+1], i, j+1))
                visit[(i,j+1)] = 1
            if i > 0 and (i-1,j) not in visit:
                visit[(i-1,j)] = 1
                heapq.heappush(s, (g[i-1][j],i-1,j))
            if j>0 and (i, j-1) not in visit:
                visit[(i,j-1)] = 1
                heapq.heappush(s, (g[i][j-1], i, j-1))

        return b