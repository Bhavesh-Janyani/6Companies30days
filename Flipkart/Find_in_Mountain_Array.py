# Runtime = 23ms (99.10%) 
# Memory = 14.8MB (54.61%)

class Solution:
    def findInMountainArray(self, target: int, nums: 'MountainArray') -> int:
        n=nums.length()
        l,r=0,n-1
        while l<r:
            m=(l+r)//2
            if nums.get(m)<nums.get(m+1):
                l=peak=m+1
            else:
                r=m
        
        l,r=0,peak
        while l<=r:
            m=(l+r)//2
            if nums.get(m)<target:
                l=m+1
            elif nums.get(m)>target:
                r=m-1
            else:
                return m
        
        l,r=peak,n-1
        while l<=r:
            m=(l+r)//2
            if nums.get(m)>target:
                l=m+1
            elif nums.get(m)<target:
                r=m-1
            else:
                return m
        return -1