# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, sumSoFar, path):
            nonlocal res
            if not node:
                return

            sumSoFar += node.val
            path.append(node.val)
            if not node.left and not node.right:
                if sumSoFar == targetSum:
                    res.append(path[:])

            dfs(node.left, sumSoFar, path)
            dfs(node.right, sumSoFar, path)
            path.pop()

        dfs(root, 0, [])
        return res
