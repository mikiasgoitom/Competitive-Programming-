# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = []

        def searcher(root):
            if not root:
                return None
            
            if root.val > val:
                return searcher(root.left)
            elif root.val < val:
                return searcher(root.right)
            elif root.val == val:
                return root

        arr = searcher(root)
        return arr




        
                