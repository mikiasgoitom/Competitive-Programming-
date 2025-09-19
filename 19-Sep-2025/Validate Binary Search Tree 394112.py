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
        def check_BST(node):
            if not node:
                return True

            if node.left:
                # print(node.val, parent.val, node.left.val)
                if not check_BST(node.left):
                    return False
            
            if inorder and node.val <= inorder[-1]:
                return False
            
            inorder.append(node.val)
            
            if node.right:
                if not check_BST(node.right):
                    return False
            
            return True
            
        # print(inorder)

        value = check_BST(root)
        
        return value