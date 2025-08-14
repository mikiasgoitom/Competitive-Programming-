# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def dfs(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)
        # print(graph)
        new_root = target.val
        qu = deque([new_root])
        visited = set()
        while qu and k > 0:
            sz = len(qu)
            for _ in range(sz):
                cur = qu.popleft()
                # print(cur)
                visited.add(cur)
                for neb in graph[cur]:
                    if neb not in visited:
                        qu.append(neb)
            k -= 1
        ans = []
        while qu:
            ans.append(qu.pop())
        return ans



