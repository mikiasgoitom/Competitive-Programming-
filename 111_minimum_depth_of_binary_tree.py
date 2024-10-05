from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth(root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
def min_depth_recursion(root: Optional[TreeNode]) -> int:
    if not root:
            return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return 1 + min_depth_recursion(root.right)
    if not root.right:
        return 1 + min_depth_recursion(root.left)
    return 1+ min(min_depth_recursion(root.left), min_depth_recursion(root.right))
