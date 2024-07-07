# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(n1,n2):
            if not n1 or not n2:
                return n1 == n2

            if n1.val != n2.val:
                return False
            return sym(n1.left,n2.right) and sym(n1.right,n2.left)
        return sym(root.left,root.right) 
