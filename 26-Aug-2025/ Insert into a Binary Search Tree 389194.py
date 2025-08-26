# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert_node(child, parent):
            if not root:
                new_node = TreeNode(val)
                if parent.val < 
            if root.val > val:
                insert_node(root.left, root)
            elif root.val < val:
                insert_node(root.right, root)

            return root
        root = insert_node(root)
        return root

