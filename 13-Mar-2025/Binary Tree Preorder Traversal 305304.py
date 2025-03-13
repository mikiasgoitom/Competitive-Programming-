# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        trav = root
        ans = []
        if trav:
            ans.append(trav.val)
            if trav.left:
                ans.extend(self.preorderTraversal(trav.left))
            if trav.right: 
                ans.extend(self.preorderTraversal(trav.right))
                
        return ans