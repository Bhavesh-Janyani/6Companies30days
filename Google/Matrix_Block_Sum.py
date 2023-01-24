# Runtime = 97ms (96.80%) 
# Memory = 15.3MB (27.26%)

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = [[0]*(len(mat[0]) + 1)] + [[0] + row[:] for row in mat]
        for r in range(1, len(m)):
            for c in range(1, len(m[0])):
                m[r][c] += m[r-1][c] + m[r][c-1] - m[r-1][c-1]
        R, C = len(mat), len(mat[0])
        for i in range(R):
            min_r, max_r = max(0, i - K), min(R, i + K + 1)
            for j in range(C):
                min_c, max_c = max(0, j - K), min(C, j + K + 1)
                mat[i][j] = m[max_r][max_c] - m[min_r][max_c] - m[max_r][min_c] + m[min_r][min_c]
                
        return mat