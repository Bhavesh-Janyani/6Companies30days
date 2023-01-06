# Runtime = 260ms (100%) 
# Memory = 19.3MB (78.26%)

class Solution(object):
    def isRectangleCover(self, rectangles):
        corner=set()
        a,b,c,d,area=float('inf'),float('inf'),float('-inf'),float('-inf'),0
        for x1,y1,x2,y2 in rectangles:
            if x1<=a and y1<=b: a,b=x1,y1
            if x2>=c and y2>=d: c,d=x2,y2
            area+=(x2-x1)*(y2-y1)
            corner^={(x1,y1),(x2,y2),(x1,y2),(x2,y1)}
        return corner=={(a,b),(c,d),(a,d),(c,b)} and area==(c-a)*(d-b)