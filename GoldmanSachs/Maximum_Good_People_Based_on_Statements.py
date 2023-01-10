# Runtime = 469ms (94.32%) 
# Memory = 13.9MB (84.9%)

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n=len(statements)
        ans=0            
        bad_persons=[0]*n
        good_persons=[0]*n
        for i in range(n):
            good=1<<i
            bad=0
            for j in range(n):
                if statements[i][j]==2:
                    continue
                if statements[i][j]==1:
                    good|=(1<<j)
                else:
                    bad|=(1<<j)
            good_persons[i]=good
            bad_persons[i]=bad
                     
        def dfs(i,good,bad,mask,cnt):
            if i==n:
                if good==mask and good&bad==0:
                    nonlocal ans
                    ans=max(ans,cnt)
                return
            dfs(i+1,good,bad|(1<<i),mask,cnt)
            dfs(i+1,good|good_persons[i],bad|bad_persons[i],mask|(1<<i),cnt+1)
                
        dfs(0,0,0,0,0)
        return ans                  
                        
   