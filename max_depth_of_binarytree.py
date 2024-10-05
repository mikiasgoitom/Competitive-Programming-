from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
        def depthSearch(node, depth):
            if not node:
                return depth
            left_depth = depthSearch(node.left, depth+1)
            right_depth = depthSearch(node.right, depth+1)
            return max(left_depth, right_depth)
        return depthSearch(root, 0)