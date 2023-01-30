# Runtime = 135ms (97.24%) 
# Memory = 24.1MB (96.69%)

class Solution:
    def __init__(self, radius, x_center, y_center):
        self.r, self.x, self.y = radius, x_center, y_center
    def randPoint(self):
        theta = uniform(0,2*pi)
        R = self.r*sqrt(uniform(0,1))
        return [R * math.cos(theta) + self.x, R * math.sin(theta) + self.y ]
