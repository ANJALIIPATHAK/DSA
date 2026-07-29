# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def buildParent(node):
            nonlocal parent
            if not node:
                return
            
            if node.left:
                parent[node.left] = node
                buildParent(node.left)
            
            if node.right:
                parent[node.right] = node
                buildParent(node.right)

        buildParent(root)

        q = deque([target])
        distance = 0
        visited = set()
        visited.add(target)
        while(q):
            if distance == k:
                return [node.val for node in q]
            for i in range(len(q)):
                node = q.popleft()
                neighbours = [node.left, node.right, parent.get(node)]
                for n in neighbours:
                    if n and n not in visited:
                        q.append(n)
                        visited.add(n)
            distance += 1
        return []



            