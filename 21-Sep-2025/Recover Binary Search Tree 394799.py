# Problem: Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #moris traversal
        node = root
        prev = None
        n1, n2 = None, None
        
        while node:
            if not node.left:
                
                if prev and prev.val > node.val:
                    if n1 is None:
                        n1 = prev
                    n2 = node

                prev = node
                node = node.right
            else:
                pred = node.left

                while pred.right and pred.right != node:
                    pred = pred.right

                if pred.right == node:
                    pred.right = None
                    
                    if prev and prev.val > node.val:
                        if n1 is None:
                            n1 = prev
                        n2 = node
                    prev = node
                    node = node.right

                else:
                    pred.right = node
                    node = node.left
            
        n1.val, n2.val = n2.val, n1.val