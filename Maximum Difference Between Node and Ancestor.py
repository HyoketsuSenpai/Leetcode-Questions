# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node,mn,mx):
            nonlocal ans
            ans = max(abs(node.val - mx),abs(node.val - mn),ans)
            mn = min(mn,node.val)
            mx = max(mx,node.val)
            if node.left:
                dfs(node.left,mn,mx)
            if node.right:
                dfs(node.right,mn,mx)
        dfs(root,root.val,root.val)
        return ans
