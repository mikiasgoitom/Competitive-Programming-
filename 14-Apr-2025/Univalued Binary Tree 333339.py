# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        vals = 0
        if root:
            vals = root.val
        else:
            return True

        qu = deque([root])

        while qu:
            qsz = len(qu)
            for _ in range(qsz):
                print(len(qu))
                node = qu.popleft()

                if vals != node.val:
                    return False

                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)

        return True


