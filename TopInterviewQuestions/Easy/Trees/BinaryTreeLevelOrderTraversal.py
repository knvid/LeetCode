# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans=[]
        q= deque([root])
        while q:
            currLevel=[]
            for _ in range(len(q)):
                node= q.popleft()
                currLevel.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                
                if node.right is not None:
                    q.append(node.right)
            ans.append(currLevel)
        return ans