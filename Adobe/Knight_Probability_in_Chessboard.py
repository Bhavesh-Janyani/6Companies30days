# Runtime = 171ms (91.67%) 
# Memory = 13.2MB (97.92%)

class Solution(object):
    def knightProbability(self, N, K, r, c):
        moves = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        memo, out_board_p = {(r, c): 1}, 0

        for step in range(K):
            next_memo = collections.defaultdict(int)
            for (i, j), prob in memo.items():
                for d in moves:
                    di, dj = i+d[0], j+d[1]
                    
                    if 0<=di<N and 0<=dj<N:
                        next_memo[(di,dj)] += prob * 0.125
                    else:
                    
                        out_board_p += prob * 0.125
            memo = next_memo
        return 1-out_board_p