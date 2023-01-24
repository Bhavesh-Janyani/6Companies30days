# Runtime = 3089ms (24.41%) 
# Memory = 13.9MB (94.49%)

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)

        def dfs(i, used, score):
            if i == n: return score
            res = float(-inf)
            for j, mentor in enumerate(mentors):
                if j in used: continue
                ss = sum(int(a == b) for a, b in zip(students[i], mentor))
                used.add(j)
                score += ss
                res = max(res, dfs(i + 1, used, score))
                used.remove(j)
                score -= ss
            return res
        return dfs(0, set(), 0)