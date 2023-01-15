# Runtime = 615ms (92.80%) 
# Memory = 14.2MB (77.20%)

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        d = defaultdict(str)
        for i in range(len(nums)):
            d[i] = nums[i]
        ans = []
        for j in queries:
            tmp =[x[-j[1]:] for x in nums]
            tmp = sorted(enumerate(tmp), key = lambda x: x[1])
            ans.append(tmp[j[0] - 1][0])
        return ans