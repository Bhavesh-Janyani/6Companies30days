# Runtime = 55ms (46.79%) 
# Memory = 13.8MB (76.65%)

class Solution(object):
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[i for i in range(1,10)]
        res=[]
        self.helper(res,nums,k,[],n)
        return res
    def helper(self,res,nums,k,path,t):
        if len(path)==k:
            if t==0:
                res.append(path)
        for i in range(len(nums)):
            if nums[i]>t:
                continue
            self.helper(res,nums[i+1:],k,path+[nums[i]],t-nums[i])