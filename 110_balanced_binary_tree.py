# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode) -> bool:
    def check_balance(root):
        if not root: return [True, 0]
        left, right = check_balance(root.left), check_balance(root.right)
        balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)
        return [balanced, 1 + max(left[1], right[1])]
    return check_balance(root)

def is_balanced_optimised(root:TreeNode) ->bool:
    def dfs(root):
        if not root:
            return 0
        left, right = dfs(root.left), dfs(root.right)
        while left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return 1+ max(left, right)
    return dfs(root) != -1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(17)
root.right.right.left = TreeNode(27)

# Check if the tree is balanced
result = is_balanced_optimised(root)
print("Is the tree balanced?", result)
