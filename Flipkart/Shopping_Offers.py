# Runtime = 57ms (99.48%) 
# Memory = 14MB (88.2%)

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def dp(needs):
            if tuple(needs) in self.memo:
                return self.memo[tuple(needs)]
            cost = 0
            for i, need in enumerate(needs):
                cost += need * price[i]
            for offer in special:
                for i, need in enumerate(needs):
                    if need < offer[i]:
                        break
                else:
                    new_needs = [need - offer[i] for i, need in enumerate(needs)]
                    cost = min(cost, offer[-1] + dp(new_needs))
            self.memo[tuple(needs)] = cost
            return cost
        self.memo = {}
        return dp(needs)