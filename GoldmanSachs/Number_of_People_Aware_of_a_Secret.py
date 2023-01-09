# Runtime = 27ms (92.86%) 
# Memory = 13.4MB (85.71%)

class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        dp = [1] + [0] * (n - 1)
        mod = 10 ** 9 + 7
        share = 0
        for i in range(1, n):
            dp[i] = share = (share + dp[i - delay] - dp[i - forget]) % mod
        return sum(dp[-forget:]) % mod
        