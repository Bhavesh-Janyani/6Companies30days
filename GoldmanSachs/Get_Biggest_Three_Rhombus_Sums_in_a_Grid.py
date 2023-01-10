# Runtime = 1100ms (88.46%) 
# Memory = 17.6MB (50%)

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        
        l=[] # stores the sums
        n=len(grid) # number of rows
        m=len(grid[0]) # number of cols
        
        for i in range(n):
            for j in range(m):
                # iterate over every tile
                
                # top tile point of rhombus
                ans=grid[i][j]
                l.append(grid[i][j]) # valid rhombus sum (one point)
                
                # distance var to store distance from j to both ends of rhombus
                # (used to increase size of rhombus)
                distance=1 
                
                # make sure the tile is within grid bounds
                while(i+distance<n and j-distance>=0 and j+distance<m):
                    # iterate over all possible rhombus sizes using the distance var
                    
                    a=i+distance # next row
                    b=j+distance # col to the right
                    c=j-distance # col to the left
                    
                    # right tile point of rhombus:  grid[a][b]
                    # left tile point of rhombus: grid[a][c]
                    ans+=grid[a][b]+grid[a][c]
                    
                    # a dummy variable to store the present sum of the sides
                    # (left and right tile point)
                    dumm=0    
                    while(True):
                        # iterate to find the bottom point of rhombus
                        
                        c+=1 # left tile point moves toward the right
                        b-=1 # right tile point moves toward the left
                        a+=1 # moves to the bottom (next row)
                        
                        if(c==m or b==0 or a==n):
                            break # reached bounds
                        
                        # left and right cols met at "middle"
                        if(c==b): # found the bottom tile point of rhombus
                            # add bottom tile sum to sides (left and right) sum
                            dumm+=grid[a][b] 
                            l.append(ans+dumm) #appending the obtained sum
                            break
                            
                        dumm+=grid[a][b]+grid[a][c] # adding both sides sum to dummy
                        
                    distance+=1
                    
        l=list(set(l)) # remove duplicates
        l.sort(reverse=True) 
        # return first 3 largest sums
        return l[:3]