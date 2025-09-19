# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        nodes = []
        unique = set()
        def check_BST(node):
            if not node:
                return
            if node.left:
                # print(node.val, parent.val, node.left.val)
                check_BST(node.left)
            
            nodes.append(node.val)
            if node.val not in unique:
                inorder.append(node.val)
                unique.add(node.val)
            
            if node.right:
                check_BST(node.right)
            
        
        check_BST(root)
        # print(inorder, unique)
        if inorder == sorted(nodes):
            return True
        else:
            return False