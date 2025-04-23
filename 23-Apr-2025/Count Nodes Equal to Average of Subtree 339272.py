# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        n = 0
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                ans += 1
                return
            lvls = 1
            sums = node.val
            if node.left:
                s, l = dfs(node.left)
                sums += s
                lvls += l
            
            if node.right:
                s, l = dfs(node.right)
                sums += s
                lvls += l
            
            if floor(sums / lvls) == node.val:
                ans += 1
            
            # print("dsd", node.val, ans, sums, lvls)

            return sums, lvls
        
        dfs(root)
        return ans
            

