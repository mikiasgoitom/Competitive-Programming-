# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        def count_d(root):
            if  not root:
                return 0
            
            c_l = count_d(root.left)
            c_r = count_d(root.right)

            count = max(c_l, c_r)
            return count + 1
        count = count_d(root)
        return count

            