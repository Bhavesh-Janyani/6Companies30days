# Runtime = 515ms (62.90%) 
# Memory = 14.3MB (90.32%)

class Solution(object):
    def findTheCity(self, n, edges, maxd):
        dis = [[float('inf')] * n for _ in xrange(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in xrange(n):
            dis[i][i] = 0
        for k in xrange(n):
            for i in xrange(n):
                for j in xrange(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= maxd for d in dis[i]): i for i in xrange(n)}
        return res[min(res)]