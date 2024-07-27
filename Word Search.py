class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        lb = len(board)
        llb = len(board[0])

        def bt(i,j,visited,s,k):
            nonlocal ans
            if k == len(word):
                ans = True
                return
            if i >= lb or i < 0:
                return
            if j >= llb or j < 0:
                return
            
            
            s += board[i][j]
            
            if s == word:
                
                ans = True
                return
            if s[k] != word[k]:
                
                return
            visited.add((i,j))
            
            if (i + 1,j) not in visited:
                bt(i + 1,j,visited,s,k + 1)
            if (i - 1,j) not in visited:
                bt(i - 1,j,visited,s,k + 1)
            if (i,j + 1) not in visited:
                bt(i,j + 1,visited,s,k + 1)
            if (i,j - 1) not in visited:
                bt(i,j - 1,visited,s,k + 1)

            visited.remove((i,j))

        for i in range(lb):
            for j in range(llb):
                if board[i][j] == word[0]:
                    bt(i,j,set(),'',0)
        return ans
        
            
            
