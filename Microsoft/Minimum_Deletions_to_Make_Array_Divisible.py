# Runtime = 884ms (86.14%) 
# Memory = 26MB (54.82%)

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        a = sorted(numsDivide)
        b = sorted(nums)
        count = 0
        gcd=a[0]
        for i in numsDivide:
            gcd = math.gcd(gcd, i)
        print(gcd)
        for i in b:
            if gcd % i == 0:
                break
            else:
                count += 1
        if count == len(nums):
            return(-1)
        else:
            return(count)      
        