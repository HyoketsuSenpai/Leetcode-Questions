# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        rep = defaultdict(int)
        def dfs(node):
            if node == None:
                return
            rep[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        mx = max(rep.values())
        ans = []
        for n in rep.keys():
            if rep[n] == mx:
                ans.append(n)
        return ans
