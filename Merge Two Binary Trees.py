# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = TreeNode()
        def dfs(n1,n2,ans):
            if n1 and n2:
                ans = TreeNode(n1.val + n2.val)
                ans.left = dfs(n1.left,n2.left,ans.left)
                ans.right = dfs(n1.right,n2.right,ans.right)
            elif n1:
                ans = TreeNode(n1.val)
                ans.left = n1.left
                ans.right = n1.right
            elif n2:
                ans = TreeNode(n2.val)
                ans.left = n2.left
                ans.right = n2.right
            else:
                ans = None
            return ans
        return dfs(root1,root2,ans)
        return ans
        
