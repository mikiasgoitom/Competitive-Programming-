# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inord_res = []

        curr = root
        stk = []
        
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            inord_res.append(curr.val)
            curr = curr.right
        
        def buildbbst(nums, l, r):
            if l > r:
                return
            
            mid = (r + l) // 2
            node = TreeNode(nums[mid])
            node.left = buildbbst(nums, l, mid - 1)
            node.right = buildbbst(nums, mid + 1, r)

            return node
        bnode = buildbbst(inord_res, 0, len(inord_res) - 1)

        return bnode