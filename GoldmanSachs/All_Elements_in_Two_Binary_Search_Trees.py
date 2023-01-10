# Runtime = 360ms (80.79%) 
# Memory = 17.8MB (98.73%)

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        st1, st2 = [], []
        res = []
        
        while root1 != None or root2 != None or len(st1) > 0 or len(st2) > 0:
            while root1 != None:
                st1.append(root1)
                root1 = root1.left
            while root2 != None:
                st2.append(root2)
                root2 = root2.left
            if len(st2) == 0 or (len(st1) > 0 and st1[-1].val <= st2[-1].val):
                root1 = st1.pop()
                res.append(root1.val)
                root1 = root1.right
            else:
                root2 = st2.pop()
                res.append(root2.val)
                root2 = root2.right
        return res