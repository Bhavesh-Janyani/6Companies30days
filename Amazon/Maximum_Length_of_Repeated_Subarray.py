# Runtime = 573ms (93.4%) 
# Memory = 19.7MB (79.41%)

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def can(mi):
            subs1 = {tuple(nums1[i-mi:i]) for i in range(mi, len(nums1) + 1)}
            subs2 = {tuple(nums2[i-mi:i]) for i in range(mi, len(nums2) + 1)}
            return subs1 & subs2
        lo, hi = 0, min(len(nums1), len(nums2)) + 1
        while hi - lo > 1:
            mi = lo + hi >> 1
            if can(mi):
                lo = mi
            else:
                hi = mi
        return lo