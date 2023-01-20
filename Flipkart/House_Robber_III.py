# Runtime = 28ms (93.84%) 
# Memory = 17.4MB (83.41%)

class Solution(object):
    def rob(self, root):
        def robHelper(root):
            if not root:
                return (0, 0)
            left, right = robHelper(root.left), robHelper(root.right)
            return (root.val + left[1] + right[1], max(left) + max(right))

        return max(robHelper(root))