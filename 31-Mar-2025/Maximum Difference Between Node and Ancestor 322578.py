# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff = 0
        def dfs(node):
            if not node:
                return [float('inf'), float('-inf')]
            if not node.left and not node.right:
                return [node.val, node.val]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            nonlocal diff
            
            min_val = min(left[0], right[0], node.val)
            max_val = max(left[1], right[1],  node.val)

            diff = max(diff, max(abs(min_val - node.val), abs(max_val - node.val)))  

            return [min_val, max_val]
        
        dfs(root)
        return diff