# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        accum = 0
        ac = []
        curr = root
        stk = []
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.right
            
            curr = stk.pop()
            print("a", curr.val, accum)
            curr.val += accum
            accum = curr.val
            print("b", curr.val, accum)
            ac.append(accum)
            curr = curr.left
        # print(ac)
        return root

