# Runtime = 2330ms (92.65%) 
# Memory = 43.8MB (19.12%)

from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N, output = len(nums2), 0
        idx_nums2 = {nums2[i]: i for i in range(N)}
        nums = []
        for i in range(N):
            nums.append(idx_nums2[nums1[i]])

        smaller = self.countSmallerLeft(nums)
        greater = self.countGreaterRight(nums)

        for i in range(1, N):
            output += smaller[i] * greater[i]
        return output
        
    def countSmallerLeft(self, nums: List[int]) -> List[int]:
        N, output, multiset = len(nums), [None] * len(nums), SortedList()
        for i in range(0, N):
            idx = multiset.bisect_left(nums[i])
            output[i] = idx
            multiset.add(nums[i])
        return output

    def countGreaterRight(self, nums: List[int]) -> List[int]:
        N, output, multiset = len(nums), [None] * len(nums), SortedList()
        for i in range(N - 1, -1, -1):
            idx = multiset.bisect_left(nums[i])
            output[i] = len(multiset) - idx
            multiset.add(nums[i])
        return output