# Runtime = 34ms (88.35%) 
# Memory = 13.8MB (74.8%)

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [x for x in range(1,n+1)]
        start = -1
        while len(nums)>1:
            if start+k<len(nums):
                start = start+k
                val = nums[start]
                start-=1
            else:
                start = (start+k)%len(nums)
                start-=1
            nums.pop(start+1)
        return(nums[0])