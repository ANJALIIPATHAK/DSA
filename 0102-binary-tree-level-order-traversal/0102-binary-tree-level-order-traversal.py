# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        if(not root):
            return res

        while(q):
            sameLevel = []
            for _ in range(len(q)):
                currNode = q.popleft()
                sameLevel.append(currNode.val)
                if(currNode.left):
                    q.append(currNode.left)
                if(currNode.right):
                    q.append(currNode.right)
            res.append(sameLevel)
        return res


        