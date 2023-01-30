# Runtime = 1176ms (88.96%) 
# Memory = 26.2MB (89.30%)

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res, stack, prefix = 0, [], [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        for i, n in enumerate(nums):
            newStart = i
            while stack and stack[-1][1] > n:
                start, val = stack.pop()
                total = prefix[i] - prefix[start]
                res = max(res, val * total)
                newStart = start
            stack.append((newStart, n))
        for start, val in stack:
            total = prefix[len(nums)] - prefix[start]
            res = max(res, val * total)
        return res % (10**9 + 7)