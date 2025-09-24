# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dp(node):
            if node is None:
                return 0

            if node not in memo:
                opt1 = dp(node.left) + dp(node.right)
                opt2 = node.val

                if node.left and node.right:
                    # print("1q")
                    opt2 += dp(node.left.left) + dp(node.left.right) +  dp(node.right.left) +  dp(node.right.right)
                elif node.left:
                    # print("1w")
                    opt2 += dp(node.left.left) +  dp(node.left.right)
                elif node.right:
                    # print("1e")
                    opt2 += dp(node.right.left) +  dp(node.right.right)

                # print(opt1, opt2)
                memo[node] = max(opt1, opt2)
            return memo[node]
        return dp(root)
        # print(memo)
        