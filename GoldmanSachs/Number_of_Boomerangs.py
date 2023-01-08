# Runtime = 657ms (84.62%) 
# Memory = 13.8MB (23.8%)

class Solution(object):
    def numberOfBoomerangs(self, points):
        nums = 0
        for x1, y1 in points:
            distance = collections.defaultdict(int)
            for x2, y2 in points:
                dx = abs(x2 - x1)
                dy = abs(y2 - y1)
                d = dx * dx + dy * dy
                distance[d] += 1

            nums += sum(n * (n-1) for n in distance.values())
        return nums