# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        
        q.append(root)
        while q:
            qlen = len(q)

            lvl = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    lvl.append(node.val)
            ans.append(lvl)
        for i in range(len(ans)):
            if i % 2:
                ans[i].reverse()
        ans.pop()
        return ans
