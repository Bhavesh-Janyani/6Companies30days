# Runtime = 160ms (82.29%) 
# Memory = 14.8MB (47.92%)

class Solution(object):
    def findUnsortedSubarray(self, nums):
        if len(nums) < 2: return 0
        l, r = 0, len(nums) - 1
        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1
        while r > 0 and nums[r] >= nums[r -1]:
            r -= 1
        if l > r:
            return 0
        temp = nums[l:r+1]
        tempMin = min(temp)
        tempMax = max(temp)
        while l > 0 and tempMin < nums[l-1]:
            l -= 1
        while r < len(nums) - 1 and tempMax > nums[r+1]:
            r += 1
        return r - l + 1