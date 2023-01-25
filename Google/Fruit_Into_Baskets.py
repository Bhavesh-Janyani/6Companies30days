# Runtime = 814ms (57.57%) 
# Memory = 19MB (97.79%)

class Solution(object):
    def totalFruit(self, fruits):
        n = len(fruits)
        type1 = fruits[0]
        type2 = -1
        curLen = 1
        maxi = 1
        combo = 1
        for i in range(1,n):
            if ((fruits[i]!= type1) and (fruits[i]!= type2) and (type2 !=-1)):
                maxi = max(curLen,maxi)
                curLen = combo +1
                type2 = type1
                type1 = fruits[i]
                combo = 1 
                continue
            if fruits[i] == type1 :
                combo+=1
            else:
                
                type2 = type1
                type1 = fruits[i]
                combo = 1
            curLen+=1
        return max(maxi,curLen)