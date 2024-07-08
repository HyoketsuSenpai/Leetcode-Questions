# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node,lvl):
            if len(ans) == lvl:
                ans.append(node.val)
            if node.right:
                dfs(node.right,lvl + 1)
            if node.left:
                dfs(node.left,lvl + 1)
            
        if root:
            dfs(root,0)
        return ans
