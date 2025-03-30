# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        q = deque([(root.left, root.right)])

        while q:
            print(q)
            left, right = q.popleft()

            if not left and not right:
                continue
            
            if not left or not right or left.val != right.val:
                return False

            q.append((left.left, right.right))
            q.append((left.right, right.left))
        
        return True
