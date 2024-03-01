# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        level=[(root,None,None)]
        
        while level:
            level2 = []
            for k,floor,ceil in level:
                
                if k.left:
                    if k.left.val >= k.val or floor is not None and k.left.val <= floor:
                        return False
                    level2.append((k.left,floor,k.val))
                    
                if k.right:
                    if k.right.val <= k.val or ceil is not None and k.right.val >= ceil:
                        return False
                    level2.append((k.right,k.val,ceil))

                level = level2
                    
        return True