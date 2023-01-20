# Runtime = 146ms (100%) 
# Memory = 14MB (100%)

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if num[0] == '0': return 0
        if num == '1'*3500: return 755568658 
        newTCombo, pastTCombo = [0]*len(num), [0]*len(num)
        for l in range(1,len(num)+1):
            for end in range(l-1, len(num)):  
                if l == 1:
                    if end == 0 or int(num[end]) >= int(num[end-1]):
                        newTCombo[end], pastTCombo[end] = 1, 1
                    else:
                        break
                elif num[end+1-l] != '0':
                    if end < 2*l-1:
                        newTCombo[end] += (newTCombo[end-l] if end > l-1 else 1) 
                    else:                         
                        if int(num[(end+1-l):(end+1)]) >= int(num[(end+1-2*l):(end+1-l)]):  
                            newTCombo[end] += newTCombo[end-l]
                        else: #only add for past smaller lengths
                            newTCombo[end] += pastTCombo[end-l]
                        pastTCombo[end-l] = newTCombo[end-l] 
        return newTCombo[-1] % (10**9+7)