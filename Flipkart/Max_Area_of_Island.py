# Runtime = 88ms (98.7%) 
# Memory = 13.7MB (92.49%)

class Solution(object):
    def maxAreaOfIsland(self, grid):
        row, col = len(grid), len(grid[0])
        result = 0
        visited = [[0 for j in range(col)] for i in range(row)]
        result = 0
        queue = []

        for i in range(row):
            for j in range(col):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    queue.append((i,j))
                    visited[i][j] = 1
                    current_area = 0
                    while queue:
                        current_area += 1
                        node = queue.pop(0)
                        i , j = node[0], node[1]
                        
                        if i - 1 >=0 and visited[i-1][j] == 0 and grid[i-1][j] == 1:
                            queue.append((i-1,j))
                            visited[i-1][j] = 1
                        if i + 1 < row and visited[i+1][j] == 0 and grid[i+1][j] == 1:
                            queue.append((i+1,j))
                            visited[i+1][j] = 1
                        if j - 1 >= 0 and visited[i][j-1] == 0 and grid[i][j-1] == 1:
                            queue.append((i, j-1))
                            visited[i][j-1] = 1
                        if j + 1 < col and visited[i][j+1] == 0 and grid[i][j+1] == 1:
                            queue.append((i, j+1))
                            visited[i][j+1] = 1
                    result = max(current_area, result)
        return result