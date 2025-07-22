# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque()
        q.append(root)

        if(not root):
            return res

        while(q):
            rightNode = None
            for _ in range(len(q)):
                currNode = q.popleft()
                if(currNode.left):
                    q.append(currNode.left)
                if(currNode.right):
                    q.append(currNode.right)
            if(currNode):
                rightNode = currNode
                res.append(rightNode.val)
        return res