# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert_node(root):
            if not root:
                return TreeNode(val)
            
            if root.val > val:
                root.left = insert_node(root.left)
            elif root.val < val:
                root.right  =  insert_node(root.right)
            return root
        root = insert_node(root)
        return root

