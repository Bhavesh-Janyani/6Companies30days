# Runtime = 90ms (94.37%) 
# Memory = 13.9MB (62.68%)

class Solution(object):
    def closedIsland(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_isl = 0

        def dfs(r,c):
            if grid[r][c] == 1:
                return True
            if r <= 0 or r >= num_rows-1 or c <= 0 or c >= num_cols-1:
                return False
            grid[r][c] = 1
            up=dfs(r-1, c)
            down=dfs(r+1, c)
            left=dfs(r, c-1)
            right=dfs(r, c+1)
            return left and right and up and down
        for row in range(1, num_rows-1):
            for col in range(1, num_cols-1):
                if grid[row][col]==0 and dfs(row, col):
                    num_isl+=1
        return num_isl