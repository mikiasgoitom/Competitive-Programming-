# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_arr = []
        q_arr = []
        def dfs(node):
            if not node:
                return
            
            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if right and left:
                return node

            return left if left else right
            
        return dfs(root)
