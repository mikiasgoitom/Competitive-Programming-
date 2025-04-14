# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        qu = deque([root])
        ans = []

        while qu:
            qsz = len(qu)
            temp = []
            for _  in range(qsz):
                node = qu.popleft()
                temp.append(node.val)

                if node.left:
                    qu.append(node.left)
                
                if node.right:
                    qu.append(node.right)
                
            ans.append(temp)
        
        return ans

