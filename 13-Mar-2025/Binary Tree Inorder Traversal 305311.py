# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        trav = root
        ans = []
        if trav:
            ans.extend(self.inorderTraversal(trav.left))
            ans.append(trav.val)
            ans.extend(self.inorderTraversal(trav.right))
        
        return ans
