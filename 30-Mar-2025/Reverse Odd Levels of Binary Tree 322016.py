# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left, right, n):
            if not left or not right:
                return 
            
            if n % 2 != 0:
                temp = left.val
                left.val = right.val
                right.val = temp
            
            dfs(left.left, right.right, n + 1)
            dfs(left.right, right.left, n + 1)
        
        dfs(root.left, root.right, 1)
        return root



