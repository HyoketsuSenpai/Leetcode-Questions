# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def val(node):
            if not node:
                return []
            
            l = val(node.left)
            l.append(node.val)
            l+=val(node.right)
            return l
        r = val(root)
        return r == sorted(r) and len(r) == len(set(r))
