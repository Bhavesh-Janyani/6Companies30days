# Runtime = 164ms (90.12%) 
# Memory = 13.9MB (70.37%)

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        currMax = 0
        result = [[0]*12]

        def maxscore(section, score, arrows, i):
            nonlocal currMax
            if arrows < 0:
                return
            if arrows == 0 or i == 0:
                if score >= currMax:
                    currMax = score
                    if arrows > 0:
                        result[0] = [arrows] + section[1:]
                    else:
                        result[0] = section[:]
                return
            section[i] = aliceArrows[i]+1
            maxscore(section, score+i, arrows-aliceArrows[i]-1, i-1)
            section[i] = 0
            maxscore(section, score, arrows, i-1)
        
        maxscore([0]*12, 0, numArrows, 11)
        return result[0]