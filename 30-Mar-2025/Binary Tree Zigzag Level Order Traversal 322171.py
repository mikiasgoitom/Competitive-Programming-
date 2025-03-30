# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        toggle = True
        res = [[root.val]]
        while q:
            qs = len(q)
            temp = []
            for _ in range(qs):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    temp.append(node.left.val)
                
                if node.right:
                    q.append(node.right)
                    temp.append(node.right.val)
            if temp:
                if toggle:
                    rev_temp = list(reversed(temp))
                    res.append(rev_temp)
                else:
                    res.append(temp)
            toggle = not toggle
        return res

