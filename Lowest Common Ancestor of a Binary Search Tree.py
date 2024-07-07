# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def go(node):
            nonlocal p
            nonlocal q
            if not node:
                return node
            if node.val > p.val and node.val > q.val:
                return go(node.left)
            if node.val < p.val and node.val < q.val:
                return go(node.right)
            return node
        return go(root)
