# Runtime = 28ms (89.16%) 
# Memory = 13.9MB (9.51%)

class Solution:
    def decToBase(self, n: int, base: int) -> int:
        ans = ""
        while n:
            n, rem = divmod(n, base)
            ans = str(rem) + ans
        return ans

    def isPalindromeString(self, s):
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n-1):
            n_in_base = self.decToBase(n, base)
            if not self.isPalindromeString(n_in_base):
                return False
        return True