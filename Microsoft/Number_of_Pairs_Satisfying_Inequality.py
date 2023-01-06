# Runtime = 2861ms (51.6%) 
# Memory = 33.4MB (20.42%)

from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        sl, ans = SortedList(), 0
        for num1, num2 in zip(nums1, nums2):
            ans += sl.bisect_right(num1 - num2 + diff)
            sl.add(num1 - num2)
        return ans
        
# Time Complexity: O(NlogN)
# Space Complexity: O(N)